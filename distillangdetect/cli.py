# coding: utf-8
from __future__ import unicode_literals

import os
import json
import click
import shutil

from distillangdetect import config
model_config = config.ModelDownloadConfig()

@click.group()
def main():
    pass

@main.command()
@click.option("--model_name", "-m", required=True, type=str, help="Name of model you want to use from: {}".format(list(model_config.get_model_list())))
def download(model_name):
    if model_config.check_model_presence(model_name):
        model_dropbx_link = model_config.get_model_link(model_name)
        distillangdetect_model_dir = model_config.get_model_path(model_name)
        distillangdetect_model_parent = os.path.dirname(distillangdetect_model_dir)
        
        if os.path.exists(distillangdetect_model_dir):
            integrity, distillangdetect_model_dir = model_config.get_model_path_and_varify_integrity(model_name)
            if not integrity:
                print("Model path already exists, but files verification failed, removing directory and reinstalling model.")
                shutil.rmtree(distillangdetect_model_dir)
            else:
                print("Model {} already exists at {}, integrity varified.".format(model_name, distillangdetect_model_dir))
                return    

        if not os.path.exists(distillangdetect_model_parent):
            os.makedirs(distillangdetect_model_parent)
        os.system("wget -O {}.zip {}".format(distillangdetect_model_dir, model_dropbx_link))
        
        if not os.path.exists(distillangdetect_model_dir):
            os.makedirs(distillangdetect_model_dir)
        
        os.system("unzip {}.zip -d {}/".format(distillangdetect_model_dir, distillangdetect_model_dir))
        os.remove(distillangdetect_model_dir+".zip")
        
        print("Model {} downloaded successfully".format(model_name))
    else:
        print("Model name you've specified is not available. Specify one from {}".format(model_config.get_model_list()))    

if __name__ == '__main__':
    main()