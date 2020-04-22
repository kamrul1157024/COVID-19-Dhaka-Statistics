import PyPDF2 
pdfFileObj = open('C:\\Users\\Asus\\Desktop\\COVID_19\\20200418-sitrep-89-covid-19.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
print(pdfReader.numPages) 
whole_pdf_text=""
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)  
    whole_pdf_text=whole_pdf_text+pageObj.extractText();

print(whole_pdf_text);
  
pdfFileObj.close() 



# Python program for KMP Algorithm 
def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 
      lps = [0]*M 
    j = 0   
    computeLPSArray(pat, M, lps) 
  
    i = 0 
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            return (i-j)
            j = lps[j-1] 
        elif i < N and pat[j] != txt[i]: 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
  
def computeLPSArray(pat, M, lps): 
    len = 0
  
    lps[0]
    i = 1
    while i < M: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            if len != 0: 
                len = lps[len-1] 
            else: 
                lps[i] = 0
                i += 1

  
#KMP FINISH  
# txt = "ABABDABACDABABCABAB"
# pat = "ABABCABAB"
# KMPSearch(pat, txt) 


KMPSearch("Bangladesh",whole_pdf_text)


  







