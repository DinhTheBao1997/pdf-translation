from fpdf import FPDF
from fpdf.py3k import PY3K

class CustomFPDF(FPDF):
    def config(self):
        self.compress = False
        self.add_font('times', '', './static/fonts/times/times.ttf', uni=True) 
        pass

    def output(self, name='',dest=''):
        "Output PDF to some destination"
        #Finish document if necessary
        if(self.state<3):
            self.close()
        dest=dest.upper()
        if(dest==''):
            if(name==''):
                name='doc.pdf'
                dest='I'
            else:
                dest='F'
        if dest=='I':
            print(self.buffer)
        elif dest=='D':
            print(self.buffer)
        elif dest=='F':
            #Save to local file
            f=open(name,'wb')
            if(not f):
                self.error('Unable to create output file: '+name)
            if PY3K:
                # manage binary data as latin1 until PEP461 or similar is implemented
                f.write(self.buffer.encode("latin1"))
            else:
                f.write(self.buffer)
            f.close()
        elif dest=='S':
            #Return as a string
            return self.buffer
        else:
            self.error('Incorrect output destination: '+dest)
        return ''
