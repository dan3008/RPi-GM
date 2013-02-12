#-------------------------------------------------------------------------------
# Name:        Zipper
# Purpose:     To load and save all the files used in a game into one zip :) (or a .rpg)
#
# Author:      Daniel
#
# Created:     11/02/2013
# Copyright:   (c) Daniel 2013
# Licence:     GPL
#-------------------------------------------------------------------------------

import zipfile, os

class zipper:
    def makeArchive(self,fileList, archive,root):
        """
        'fileList' is a list of file names - full path each name
        'archive' is the file name for the archive with a full path
        """
        try:
            a = zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED)
            for f in fileList:
                print "archiving file %s" % (f)
                a.write(f, os.path.relpath(f, root))
            a.close()
            return True
        except: return False

    def dirEntries(self,dir_name, subdir, *args):
        '''Return a list of file names found in directory 'dir_name'
        If 'subdir' is True, recursively access subdirectories under 'dir_name'.
        Additional arguments, if any, are file extensions to match filenames. Matched
            file names are added to the list.
        If there are no additional arguments, all files found in the directory are
            added to the list.
        Example usage: fileList = dirEntries(r'H:\TEMP', False, 'txt', 'py')
            Only files with 'txt' and 'py' extensions will be added to the list.
        Example usage: fileList = dirEntries(r'H:\TEMP', True)
            All files and all the files in subdirectories under H:\TEMP will be added
            to the list.
        '''
        fileList = []
        for file in os.listdir(dir_name):
            dirfile = os.path.join(dir_name, file)
            if os.path.isfile(dirfile):
                if not args:
                    fileList.append(dirfile)
                else:
                    if os.path.splitext(dirfile)[1][1:] in args:
                        fileList.append(dirfile)
            # recursively access file names in subdirectories
            elif os.path.isdir(dirfile) and subdir:
                print "Accessing directory:", dirfile
                fileList.extend(self.dirEntries(dirfile, subdir, *args))
        return fileList

    def savefile(self,Dir,Zname):
        folder = Dir
        zipname = Zname
        self.makeArchive(self.dirEntries(folder, True), zipname,folder)

    def openfile (self,Dir,Zname):
        z = zipfile.ZipFile(Zname)
        z.extractall(Dir)
