#encoding=utf-8
##预处理器
from markdown.preprocessors import Preprocessor
class CodePreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        flag_in = False
        block = []
        for line in lines:
            if line[:3]=='!!!':                
                flag_in = True
                block.append('<pre class="brush: %s;">' % line[3:].strip())
            elif flag_in:
                if line.strip() and line[0]=='!':
                    block.append(line[1:])
                else:
                    flag_in = False
                    block.append('</pre>')
                    block.append(line)
                    new_lines.extend(block)
                    block = []
            else:
                new_lines.append(line)
        if not new_lines and block:
            new_lines = block
        return new_lines

##后置处理器
from markdown.postprocessors import Postprocessor
class CodePostprocessor(Postprocessor):
    def run(self, text):
        t_list = []
        for line in text.split('\n'):
            if line[:5]=='<p>!<':
                line = line.lstrip('<p>').replace('</p>', '')[1:]
            t_list.append(line) 
        return '\n'.join(t_list)    
    
##扩展主体类        
from markdown.extensions import Extension
from markdown.util import etree
class CodeExtension(Extension):
    def __init__(self, configs={}):
        self.config = configs

    def extendMarkdown(self, md, md_globals):
        ##注册扩展，用于markdown.reset时扩展同时reset
        md.registerExtension(self)   
                
        ##设置Preprocessor
        codepreprocessor = CodePreprocessor()
        #print md.preprocessors.keys()
        md.preprocessors.add('codepreprocessor', codepreprocessor, '<normalize_whitespace')
        
        ##设置Postprocessor
        codepostprocessor = CodePostprocessor()
        #print md.postprocessors.keys()
        md.postprocessors.add('codepostprocessor', codepostprocessor, '>unescape')
        
        ##print md_globals   ##markdown全局变量
        