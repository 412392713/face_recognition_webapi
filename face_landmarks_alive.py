# -*- coding: utf-8 -*-
import face_recognition
from flask import Flask, jsonify, request, redirect
from face_util import allowed_file
import os


def face_landmarks_alive():
    if request.method == 'POST':
        img1 = request.values.get("img1")

        if img1 and allowed_file(img1):
            result = {
                #landmarks : {},
                'openMouth' : False,
                'closeEyes' : False,
                'lookLeft' : False,
                'lookRight' : False
            }
            file_path = os.path.join(os.getcwd(),img1)
            landmarks = face_recognition.face_landmarks(face_recognition.load_image_file(file_path))
            #print(jsonify(landmarks))
            if len(landmarks) > 0 :
                result['landmarks'] = landmarks[0]
                #取到边框
                min_x=min_y=10000
                max_x=max_y=0
                for k in landmarks[0]:
                    for p in landmarks[0][k] : 
                        min_x = min(min_x, p[0])
                        min_y = min(min_y, p[1])
                        max_x = max(max_x, p[0])
                        max_y = max(max_y, p[1])
                #判断张嘴
                lip_top = landmarks[0]["top_lip"][9]
                lip_bottom = landmarks[0]["bottom_lip"][9]
                lip = abs((lip_top[1] - lip_bottom[1]) * 1.0 / (max_y - min_y))
                lip_n = 0.06
                if request.values.get("openMouth") :
                    lip_n = float(request.values.get("openMouth"))
                if lip > lip_n :
                    result['openMouth'] = True
                #print lip_top
                #print lip_bottom
                #print max_y
                #print min_y
                #print lip
                #print('lip=%.f' %(lip))
                #闭眼判断
                eye_right_top = landmarks[0]["left_eye"][1]
                eye_right_bottom = landmarks[0]["left_eye"][5]
                eye_left_top = landmarks[0]["right_eye"][1]
                eye_left_bottom = landmarks[0]["right_eye"][5]
                eye_right = abs((eye_right_top[1] - eye_right_bottom[1])*1.0 / (max_y - min_y))
                eye_left =  abs((eye_left_top[1] - eye_left_bottom[1])*1.0 / (max_y - min_y))
                eye_n = 0.04
                if request.values.get("closeEyes") :
                    eye_n = float(request.values.get("closeEyes"))
                if eye_right < eye_n and eye_left < eye_n :
                    result['closeEyes'] = True
                #print eye_right
                #print eye_left
                
                #左看右看
                right = landmarks[0]["chin"][0]
                left = landmarks[0]["chin"][16]

                le = abs((left[0] - eye_left_top[0])*1.0 / (max_x - min_x))
                ri = abs((right[0] - eye_right_top[0])*1.0 / (max_x - min_x))
                look_n = 0.2
                if request.values.get("lookLeftRight") :
                    look_n = float(request.values.get("lookLeftRight"))
                if le < look_n :
                    result['lookLeft'] = True
                if ri < look_n :
                    result['lookRight'] = True
                #print le
                #print ri
                
            return jsonify(result)

    return '''
    <!doctype html>
    <title>face_landmarks_alive</title>
    <h1>活体检测</h1>
    <form method="POST" enctype="multipart/form-data">
      图片路径1：<input type="text" name="img1">
      <br/><br/>
      -----------参数---------------
      <br/><br/>
      张嘴：<input type="text" name="openMouth" value="0.06">
      闭眼：<input type="text" name="closeEyes" value="0.04">
      左右看：<input type="text" name="lookLeftRight" value="0.2">
      <br/><br/>
      <input type="submit" value="提交">
    </form>
    <br/>
      <br/>
      <br/>
      --------------说明----------------------------<br/>
      结果不理想，尝试微调参数。
      
      返回：
      {
                'landmarks' : 人脸关键点坐标,
                'openMouth' : 是否张嘴,
                'closeEyes' : 是否闭眼,
                'lookLeft' : 是否向左看,
                'lookRight' : 是否向右看
            }
      <br/>
      <br/>
      <br/>
    
    '''