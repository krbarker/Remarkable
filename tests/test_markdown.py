#!usr/bin/python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2017 <Harald Weiner> <timeraider@gmx.at>
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
### END LICENSE

import pytest

import remarkable.styles 
import markdown

#html_start = ""
#html_end = ""
exts = ['markdown.extensions.extra','markdown.extensions.toc', 'markdown.extensions.smarty', 'markdown.extensions.nl2br', 'markdown.extensions.urlize', 'markdown.extensions.Highlighting', 'markdown.extensions.Strikethrough', 'markdown.extensions.markdown_checklist', 'markdown.extensions.superscript', 'markdown.extensions.subscript', 'markdown.extensions.mathjax']

#def setup_html():
#    global html_start
#    global html_end
#    html_start = 'body'

def test_markdown_normal_text1():
     text = "abc"
     html = markdown.markdown(text)
     assert html == '<p>abc</p>'

def test_markdown_normal_text2():
     text = "abc\n\ndef"
     html = markdown.markdown(text)
     assert html == '<p>abc</p>\n<p>def</p>'

def test_markdown_head1():
     text = "# title"
     html = markdown.markdown(text)
     assert html == '<h1>title</h1>'

def test_markdown_head2():
     text = "### title"
     html = markdown.markdown(text)
     assert html == '<h3>title</h3>'

def test_markdown_head3():
     text = "### title"
     html = markdown.markdown(text)
     assert html == '<h3>title</h3>'
