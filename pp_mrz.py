# -*- coding: utf-8 -*-
import face_recognition
from flask import Flask, jsonify, request, redirect
from face_util import allowed_file
from passporteye import read_mrz
import os


def pp_mrz():
    if request.method == 'POST':
        img1 = request.values.get("img1")

        if img1 and allowed_file(img1):
            file_path1 = os.path.join(os.getcwd(),img1)
            return pp_mrz_(file_path1)

    return '''
    <!doctype html>
    <title>护照MRZ识别</title>
    <h1>护照MRZ识别</h1>
    <form method="POST" enctype="multipart/form-data">
      图片路径：<input type="text" name="img1">
      <br/><br/>
      <br/><br/>
      <input type="submit" value="提交">
      <br/>
      <br/>
      <br/>
      --------------说明----------------------------
      <br/>
      返回：{"mrz":{"check_composite":"8","check_date_of_birth":"3","check_expiration_date":"0","check_number":"7","check_personal_number":"2","country":"KOR","date_of_birth":"991129","expiration_date":"230430","method":"direct","mrz_type":"TD3","names":"JAEWONK","nationality":"KOR","number":"M87540270","personal_number":"1057515V171787","sex":"M","surname":"BANG","type":"PM","valid_composite":true,"valid_date_of_birth":true,"valid_expiration_date":true,"valid_number":true,"valid_personal_number":true,"valid_score":100}}
      <br/>
      <br/>
      <br/>
    </form>
    '''

def pp_mrz_(file_path1):
    mrz = read_mrz(file_path1)

    # Return the result as json
    result = {
        "mrz": mrz.to_dict()
    }
    return jsonify(result)