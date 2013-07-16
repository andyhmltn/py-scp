py-scp
======

Do you use SCP a lot? Is your development environment layout different to wherever you usually SCP files to? Then PySCP is the script for you!

**This repo is under development so anything below this line may change when the final script is released**

Getting Started
-----------------
To get started using PySCP, you will need to create the folder mapping. To do this, run `pyscp --init`. This will create a directory in your home folder called `.pyscp` that contains the main configuration file `config.json`. Simply edit it to your needs. For example:

	{
		"directory-mapping":{
			"all":{
				// Any default mapping rules go here
			},
			"123.4.5.6":{
				"/path/to/local/directory":"/path/to/remote/directory"
			}
		}
	}

Then simply run pyscp in a similar way to how you would use the default `scp` command.  and run using `pyscp /path/to/local/directory/file.txt user@123.4.5.6`. This will scp `file.txt` to `/path/to/remote/directory` on the remote server (in this case: 123.4.5.6.)

If you wish to upload `file.txt` under a different name, you can do so by adding an extra argument to the end of the previous command. If you wanted `file.txt` to be renamed to `file_remote.txt` for example, you can use: `pyscp /path/to/local/directory/file.txt user@123.4.5.6 file_remote.txt`

Voila!

Current Version
----------------
PySCP is currently on version: `0.5.0`. To see the version of your current installation, you can run `pyscp -v`

LICENSE
----------------
The MIT License (MIT)

Copyright (c) 2013 Andy Hamilton (@ FINEIO)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
