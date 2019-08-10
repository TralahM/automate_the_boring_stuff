# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1564943191.6694126
_enable_loop = True
_template_filename = 'themes/zen/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_title', 'html_translations', 'html_sourcelink', 'html_tags', 'html_post_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        len = context.get('len', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(post.translated_to) > 1:
            __M_writer('        <div class="posttranslations translations">\n            <h3 class="posttranslations-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for langname in sorted(translations):
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <p><a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a></p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        <p class="sourceline"><a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" class="sourcelink"><i class="fa fa-file-code"></i> ')
            __M_writer(str(messages("Source")))
            __M_writer('</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags:
            __M_writer('    <div class="tags"><h3 class="metadata-title"><i class="fa fa-tags"></i> ')
            __M_writer(str(messages("Tags")))
            __M_writer(':</h3>\n        <ul itemprop="keywords" class="tags-ul">\n')
            for tag in post.tags:
                if tag not in hidden_tags:
                    __M_writer('            <li><a class="tag p-category" href="')
                    __M_writer(str(_link('tag', tag)))
                    __M_writer('" rel="tag">')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def html_sourcelink():
            return render_html_sourcelink(context)
        def html_translations(post):
            return render_html_translations(context,post)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        def html_title():
            return render_html_title(context)
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def html_tags(post):
            return render_html_tags(context,post)
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <header>\n        ')
        __M_writer(str(html_title()))
        __M_writer('\n        <div class="metadata">\n            <p class="dateline"><a href="')
        __M_writer(str(post.permalink()))
        __M_writer('" rel="bookmark"><i class="fa fa-clock"></i> <time class="published dt-published" datetime="')
        __M_writer(str(post.formatted_date('webiso')))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('">')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('</time></a></p>\n            <p class="byline author vcard"> <i class="fa fa-user"></i> <span class="byline-name fn" itemprop="author">\n')
        if author_pages_generated:
            __M_writer('                    <a href="')
            __M_writer(str(_link('author', post.author())))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('</a>\n')
        else:
            __M_writer('                    ')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('\n')
        __M_writer('            </span></p>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('                <p class="commentline"><i class="far fa-comment"></i>')
            __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer('\n')
        __M_writer('            ')
        __M_writer(str(html_sourcelink()))
        __M_writer('\n')
        if post.meta('link'):
            __M_writer('                    <p class="linkline"><a href="')
            __M_writer(str(post.meta('link')))
            __M_writer('"><i class="fa fa-link"></i> ')
            __M_writer(str(messages("Original site")))
            __M_writer('</a></p>\n')
        __M_writer('            ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n            ')
        __M_writer(str(html_tags(post)))
        __M_writer('\n        </div>\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/zen/templates/post_header.tmpl", "uri": "post_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 0, "34": 2, "35": 3, "36": 9, "37": 22, "38": 28, "39": 42, "40": 67, "46": 5, "52": 5, "53": 6, "54": 7, "55": 7, "56": 7, "57": 7, "58": 7, "64": 11, "73": 11, "74": 12, "75": 13, "76": 14, "77": 14, "78": 15, "79": 16, "80": 17, "81": 17, "82": 17, "83": 17, "84": 17, "85": 17, "86": 17, "87": 20, "93": 24, "100": 24, "101": 25, "102": 26, "103": 26, "104": 26, "105": 26, "106": 26, "112": 30, "119": 30, "120": 31, "121": 32, "122": 32, "123": 32, "124": 34, "125": 35, "126": 36, "127": 36, "128": 36, "129": 36, "130": 36, "131": 39, "137": 44, "156": 44, "157": 46, "158": 46, "159": 48, "160": 48, "161": 48, "162": 48, "163": 48, "164": 48, "165": 48, "166": 48, "167": 50, "168": 51, "169": 51, "170": 51, "171": 51, "172": 51, "173": 52, "174": 53, "175": 53, "176": 53, "177": 55, "178": 56, "179": 57, "180": 57, "181": 57, "182": 59, "183": 59, "184": 59, "185": 60, "186": 61, "187": 61, "188": 61, "189": 61, "190": 61, "191": 63, "192": 63, "193": 63, "194": 64, "195": 64, "201": 195}}
__M_END_METADATA
"""
