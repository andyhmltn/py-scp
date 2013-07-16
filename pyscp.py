#!/usr/bin/env python

import os
import sys
import json

########################
#
# Configuration
#
########################
HOME   = os.path.expanduser("~")+'/'
CONFIG = {
  'path'        : HOME+'.pyscp/',
  'config_file' : 'config.json',
  'template':{
    'directory_mapping':{
      'all':{}
    }
  }
}

########################
#
# Version function
#
########################
def fetch_version(return_version_string=True):
  VERSION = {
    'MAJOR':0,
    'MINOR':3,
    'PATCH':0
  }

  if return_version_string:
    return "PySCP Version: " + str(VERSION['MAJOR'])+'.'+str(VERSION['MINOR'])+'.'+str(VERSION['PATCH'])
  else:
    return VERSION

########################
#
# Init Script
#
########################
def install_pyscp(CONFIG):
  if not os.path.exists(CONFIG['path']):
    os.makedirs(CONFIG['path'])

    with open(CONFIG['path']+CONFIG['config_file'], 'w+') as outfile:
      json.dump(CONFIG['template'], outfile)

    print "PySCP has been installed succesfully"
  else:
    print "PySCP is already installed! Edit ~/.pyscp/config.json to begin"

########################
#
# Main PySCP Script
#
########################
def run_pyscp(arguments):
  from_path = os.path.join(os.getcwd(), arguments[1])
  to_path   = arguments[2]

  custom_filename = None

  if arguments[3] is not None:
    custom_filename = arguments[3]

  from_directory = os.path.dirname(from_path)

  directory_mapping_file = open(CONFIG['path']+CONFIG['config_file'])
  directory_mapping      = json.load(directory_mapping_file)

  remote_host_array = to_path.split("@")

  remote_host = remote_host_array[0] if len(remote_host_array) == 1 else remote_host_array[1]

  if from_directory in directory_mapping['directory_mapping']['all']:
    os.system(format_scp_string(from_path, to_path, directory_mapping['directory_mapping']['all'][from_directory]))
  else:
    if remote_host in directory_mapping['directory_mapping']:
      os.system(format_scp_string(from_path, to_path, directory_mapping['directory_mapping'][remote_host][from_directory], custom_filename))
    else:
      print "There are no rules setup for that host"

def format_scp_string(from_path,to_path,remote_path,custom_filename=None):
  # Add a trailing slash to the remote path
  if remote_path[-1] != '/':
    remote_path = remote_path + '/'

  path = "scp " + from_path + " " + to_path + ":" + remote_path
  
  if custom_filename is not None:
    path = path + custom_filename

  return path
########################
#
# Handle PySCP Arguments
#
########################
if len(sys.argv) > 1:

  if sys.argv[1] == '--init':
    install_pyscp(CONFIG)  

  elif sys.argv[1] == '-v':
    print fetch_version()

  if len(sys.argv) > 2:
    run_pyscp(sys.argv)

