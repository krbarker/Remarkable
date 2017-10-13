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

#import pytest

import remarkable.styles 
import markdown


#
# Systematically test GitHub-styled mark-down syntax
# by inferring unit tests from tutorials and guides at
#
# https://help.github.com/articles/basic-writing-and-formatting-syntax/
# and
# https://guides.github.com/features/mastering-markdown/
#


#html_start = ""
#html_end = ""
exts = ['markdown.extensions.extra','markdown.extensions.toc', 'markdown.extensions.smarty', 'markdown.extensions.nl2br', 'markdown.extensions.urlize', 'markdown.extensions.Highlighting', 'markdown.extensions.Strikethrough', 'markdown.extensions.markdown_checklist', 'markdown.extensions.superscript', 'markdown.extensions.subscript', 'markdown.extensions.mathjax']

#def setup_html():
#    global html_start
#    global html_end
#    html_start = 'body'

# only available in issues and pull-requests
#def test_markdown_at1():
#     text = '\@def'
#     html = markdown.markdown(text, exts)
#     expected = '<p>@def</p>'
#     assert html == expected

def test_markdown_at2():
     text = '`@`def'
     html = markdown.markdown(text, exts)
     expected = '<p><code>@</code>def</p>'
     assert html == expected

def test_markdown_emoji1():
     text = 'emojis: :sparkles: :camel: :boom:'
     html = markdown.markdown(text, exts)
     expected = '<p>emojis: '
     expected += '<img alt=":sparkles:" '
     expected += 'src="https://assets-cdn.github.com/images/icons/emoji/unicode/2728.png" /> '
     expected += '<img alt=":camel:" '
     expected += 'src="https://assets-cdn.github.com/images/icons/emoji/unicode/1f42b.png" /> '
     expected += '<img alt=":boom:" '
     expected += 'src="https://assets-cdn.github.com/images/icons/emoji/unicode/1f4a5.png" /> '
     expected += '</p>'
     assert html == expected

def test_markdown_bold_italic1():
     text = '**bold** *italic*'
     html = markdown.markdown(text, exts)
     expected = '<p><strong>bold</strong> <em>italic</em></p>'
     assert html == expected

def test_markdown_bold_italic2():
     text = '__bold__ _italic_'
     html = markdown.markdown(text, exts)
     expected = '<p><strong>bold</strong> <em>italic</em></p>'
     assert html == expected

def test_markdown_bold_italic3():
     text = '**This text is _extremely_ important**'
     html = markdown.markdown(text, exts)
     expected = '<p><strong>This text is <em>extremely</em> important</strong></p>'
     assert html == expected

def test_markdown_code_intend():
     text = '    if (isIll()){\n'
     text += '      stopBeingIll();\n'
     text += '      beAwesomeAgain();\n'
     text += '    }\n'
     html = markdown.markdown(text, exts)
     expected = '<pre><code>if (isIll()){\n'
     expected += '  stopBeingIll();\n'
     expected += '  beAwesomeAgain();\n'
     expected += '}\n'
     expected += '</code></pre>'
     assert html == expected

def test_markdown_code_simple():
     text = 'to list dir use `$# ls *` and that is it'
     html = markdown.markdown(text, exts)
     expected = '<p>to list dir use <code>$# ls *</code> and that is it</p>'
     assert html == expected

def test_markdown_code_multi():
     text = 'use\n```bash\n$# ls $HOME\ngit pull\n```\nand that is it'
     html = markdown.markdown(text, exts)
     expected = '<p>use</p>\n'
     expected += '<pre><code class="bash">$# ls $HOME\ngit pull\n'
     expected += '</code></pre>\n\n<p>and that is it</p>'
     assert html == expected

def test_markdown_greater1():
     text = '\> def'
     html = markdown.markdown(text, exts)
     expected = '<p>> def</p>'
     assert html == expected

def test_markdown_greater2():
     text = '`>` def'
     html = markdown.markdown(text, exts)
     expected = '<p><code>&gt;</code> def</p>'
     assert html == expected

def test_markdown_hash1():
     text = 'abc \# def'
     html = markdown.markdown(text, exts)
     expected = '<p>abc # def</p>'
     assert html == expected

def test_markdown_hash2():
     text = 'abc `#` def'
     html = markdown.markdown(text, exts)
     expected = '<p>abc <code>#</code> def</p>'
     assert html == expected

def test_markdown_head1():
     text = '# some text'
     html = markdown.markdown(text, exts)
     expected = '<h1 id="some-text">some text</h1>'
     assert html == expected

def test_markdown_head1_second():
     text = '# this is a &lt;h1&gt; tag'
     html = markdown.markdown(text, exts)
     expected = '<h1 id="this-is-a-h1-tag">this is a &lt;h1&gt; tag</h1>'
     assert html == expected

def test_markdown_head2():
     text = '### some text'
     html = markdown.markdown(text, exts)
     expected = '<h3 id="some-text">some text</h3>'
     assert html == expected

def test_markdown_head3():
     text = '### some text'
     html = markdown.markdown(text, exts)
     expected = '<h3 id="some-text">some text</h3>'
     assert html == expected

def test_markdown_head6():
     text = '###### some text'
     html = markdown.markdown(text, exts)
     expected = '<h6 id="some-text">some text</h6>'
     assert html == expected

def test_markdown_image_absolute():
     text = '![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)'
     html = markdown.markdown(text, exts)
     expected = '<p><img alt="Image of Yaktocat" '
     expected += 'src="https://octodex.github.com/images/yaktocat.png" /></p>'
     assert html == expected

def test_markdown_image_relative1():
     text = '![Image of Yaktocat](images/yaktocat.png)'
     html = markdown.markdown(text, exts)
     expected = '<p><img alt="Image of Yaktocat" '
     expected += 'src="images/yaktocat.png" /></p>'
     assert html == expected

def test_markdown_image_relative2():
     text = '![Image of Yaktocat](./images/yaktocat.png)'
     html = markdown.markdown(text, exts)
     expected = '<p><img alt="Image of Yaktocat" '
     expected += 'src="./images/yaktocat.png" /></p>'
     assert html == expected

def test_markdown_image_relative3():
     text = '![Image of Yaktocat](../images/yaktocat.png)'
     html = markdown.markdown(text, exts)
     expected = '<p><img alt="Image of Yaktocat" '
     expected += 'src="../images/yaktocat.png" /></p>'
     assert html == expected

# TODO: add more tests for hypertext links

def test_markdown_link_absolute1():
     text = 'using [GitHub Pages](https://pages.github.com/).'
     html = markdown.markdown(text, exts)
     expected = '<p>using <a href="https://pages.github.com/">GitHub Pages</a>.</p>'
     assert html == expected

def test_markdown_link_relative1():
     text = 'read [license](docs/LICENSE.md).'
     html = markdown.markdown(text, exts)
     expected = '<p>read <a href="docs/LICENSE.md">license</a>.</p>'
     assert html == expected

def test_markdown_link_relative2():
     text = 'read [license](./docs/LICENSE.md).'
     html = markdown.markdown(text, exts)
     expected = '<p>read <a href="./docs/LICENSE.md">license</a>.</p>'
     assert html == expected

def test_markdown_link_relative3():
     text = 'read [license](../docs/LICENSE.md).'
     html = markdown.markdown(text, exts)
     expected = '<p>read <a href="../docs/LICENSE.md">license</a>.</p>'
     assert html == expected

# TODO: add more tests for hypertext links

def test_markdown_list_bullet():
     text = '* One\n* Two\n* Three'
     html = markdown.markdown(text, exts)
     expected = '<ul>\n<li>One</li>\n<li>Two</li>\n<li>Three</li>\n</ul>'
     assert html == expected

def test_markdown_list_bullet():
     text = '* One\n* Two\n* Three'
     html = markdown.markdown(text, exts)
     expected = '<ul>\n<li>One</li>\n<li>Two</li>\n<li>Three</li>\n</ul>'
     assert html == expected

def test_markdown_list_bullet_nested():
     text = '* One\n  * 1.5'
     html = markdown.markdown(text, exts)
     expected = '<ul>\n<li>One</li>\n<li>Two\n'
     expected += '<ul>\n<li>2.5</li>\n</ul>\n'
     expected += '</li>\n</ul>'
     assert html == expected

def test_markdown_list_dash():
     text = '- One\n- Two\n- Three'
     html = markdown.markdown(text, exts)
     expected = '<ul>\n<li>One</li>\n<li>Two</li>\n<li>Three</li>\n</ul>'
     assert html == expected

def test_markdown_list_dash_nested():
     text = '- One\n- Two\n  - 2.5'
     html = markdown.markdown(text, exts)
     expected = '<ul>\n<li>One</li>\n<li>Two\n'
     expected += '<ul>\n<li>2.5</li>\n</ul>\n'
     expected += '</li>\n</ul>'
     assert html == expected

def test_markdown_list_numbered():
     text = '1. One\n 2. Two\n'
     html = markdown.markdown(text, exts)
     expected = '<ol>\n<li>One</li>\n<li>Two</li>\n</ol>'
     assert html == expected

def test_markdown_minus1():
     text = '\- def'
     html = markdown.markdown(text, exts)
     expected = '<p>- def</p>'
     assert html == expected

def test_markdown_minus2():
     text = '`-` def'
     html = markdown.markdown(text, exts)
     expected = '<p><code>-</code> def</p>'
     assert html == expected

def test_markdown_normal_text1():
     text = 'abc'
     html = markdown.markdown(text, exts)
     expected = '<p>abc</p>'
     assert html == expected

def test_markdown_normal_text2():
     text = 'abc\n\ndef'
     html = markdown.markdown(text, exts)
     expected = '<p>abc</p>\n<p>def</p>'
     assert html == expected

def test_markdown_quote():
     text = 'abc:\n> def\nhij\n\nklm'
     html = markdown.markdown(text, exts)
     expected = '<p>abc:</p>\n<blockquote>\n'
     expected += '<p>def<br />\nhij</p>\n</blockquote>\n'
     expected += '<p>klm</p>'
     assert html == expected

# only available in issues and pull-requests
#def test_markdown_normal_reference():
#     text = 'Hello @someuser'
#     html = markdown.markdown(text, exts)
#     expected = '<p>Hello <a href="someuser">someuser</a></p>'
#     assert html == expected

def test_markdown_star1():
     text = 'abc \* def'
     html = markdown.markdown(text, exts)
     expected = '<p>abc * def</p>'
     assert html == expected

def test_markdown_star2():
     text = 'abc `*` def'
     html = markdown.markdown(text, exts)
     expected = '<p>abc <code>*</code> def</p>'
     assert html == expected

def test_markdown_strike_through():
     text = 'abc ~~text~~ def'
     html = markdown.markdown(text, exts)
     expected = '<p>abc <del>text</del> def</p>'
     assert html == expected

def test_markdown_task_list():
     text = '- [X] Completed\n- [ ] Incomplete\n'
     html = markdown.markdown(text, exts)
     expected = '<ul class="checklist">\n'
     expected += '<li><input type="checkbox" disabled checked> Completed</li>\n'
     expected += '<li><input type="checkbox" disabled> Incomplete</li>\n'
     expected += '</ul>'
     assert html == expected
