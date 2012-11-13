# -*- coding: utf-8 -*-

# Software License Agreement (BSD License)
#
# Copyright (c) 2009-2011, Eucalyptus Systems, Inc.
# All rights reserved.
#
# Redistribution and use of this software in source and binary forms, with or
# without modification, are permitted provided that the following conditions
# are met:
#
#   Redistributions of source code must retain the above
#   copyright notice, this list of conditions and the
#   following disclaimer.
#
#   Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the
#   following disclaimer in the documentation and/or other
#   materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Andy Grimm agrimm@eucalyptus.com

import os
import sys
from euca2ools.commands.eustore.installimage import *

class InstallUnpackedImage(InstallImage):
    def bundleAll(self, dir, prefix, description, arch):
        self.destination = dir + '/'
        names = os.listdir(dir)
        import pdb; pdb.set_trace()
        kernel_dir=None
        kernel_found = False
        for path in names:
            name = path
            if name.startswith('vmlin'):
                print "Bundling/uploading kernel"
                if prefix:
                    name = prefix+name
                kernel_id = self.bundleFile(path, name, description, arch, 'true', None)
                kernel_found = True
                print kernel_id
            elif name.startswith('initr'):
                print "Bundling/uploading ramdisk"
                if prefix:
                    name = prefix+name
                ramdisk_id = self.bundleFile(path, name, description, arch, None, 'true')
                print ramdisk_id

        #now, install the image, referencing the kernel/ramdisk
        for path in names:
            name = os.path.basename(path)
            if name.endswith('.img'):
                print "Bundling/uploading image"
                if prefix:
                    name = prefix
                else:
                    name = name[:-len('.img')]
                id = self.bundleFile(path, name, description, arch, kernel_id, ramdisk_id)
                return id

if __name__ == '__main__':
    cmd = InstallUnpackedImage()
    cmd.main_cli()
