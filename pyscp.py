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
  'path'        : HOME+'.config/pyscp/',
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
def join_dict(dictionary, string='.', use_value=True):
  list_to_join = []

  for key,value in dictionary.items():
    value_to_add = value if use_value else key

    list_to_join.append(str(value))

  return string.join(list_to_join)

def fetch_version(print_version_string=True):
  VERSION = {
    'MAJOR':0,
    'MINOR':6,
    'PATCH':0
  }

  if print_version_string:
    print "PySCP Version: "+join_dict(VERSION)
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
    print "PySCP is already installed! Edit "+CONFIG['path']+CONFIG['config_file']+" to begin"

########################
#
# Main PySCP Script
#
########################
def run_pyscp(arguments, scp_flags=[]):
  from_path = os.path.join(os.getcwd(), arguments[1])
  to_path   = arguments[2]

  custom_filename = None

  if 3 in arguments:
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
      os.system(format_scp_string(from_path, to_path, directory_mapping['directory_mapping'][remote_host][from_directory], scp_flags, custom_filename))
    else:
      print remote_host
      print "There are no rules setup for that host"

def format_scp_string(from_path,to_path,remote_path,scp_flags,custom_filename=None):
  # Add a trailing slash to the remote path
  if remote_path[-1] != '/':
    remote_path = remote_path + '/'

  path = "scp " + from_path + " " + to_path + ":" + remote_path
  
  if custom_filename is not None:
    path = path + custom_filename

  for flag in scp_flags:
    path += ' '+flag

  return path

########################
#
# Handle PySCP Arguments
#
########################

flags = {
  '-v':fetch_version, 
  '--init':install_pyscp
}

scp_flags = []

arguments = sys.argv

if len(sys.argv) > 1:
  for key in arguments:
    if key in flags:
      flags[key](CONFIG)

  for key,value in enumerate(arguments):
      if value[0] == '-': #Assume it's a flag
        if value not in flags:
          scp_flags.append(value)

        del arguments[key]

  if len(arguments) > 2:
    run_pyscp(arguments, scp_flags)

