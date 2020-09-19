from PyPDF2 import PdfFileMerger
             
                
def merge(self,readFileList, _translate):
    merger = PdfFileMerger()    
    for pdf in readFileList:      
        merger.append(pdf)
    mergedfile = str(self.outputfolder)+"/"+str(self.outputFile.text())+".pdf"
    merger.write(mergedfile)
    #TODO: Ask for overwrite if file already exists
    merger.close()
