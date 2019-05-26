#!/usr/bin/env python
# -*- coding: utf-8 -*-


from functions import UploadFile

def test_upload():

    assert UploadFile.upload() == 1