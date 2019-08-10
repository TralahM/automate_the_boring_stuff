# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1564943191.845179
_enable_loop = True
_template_filename = 'themes/zen/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        pagination = _mako_get_namespace(context, 'pagination')
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        math = _mako_get_namespace(context, 'math')
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        def content_header():
            return render_content_header(context)
        pagination = _mako_get_namespace(context, 'pagination')
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        def content():
            return render_content(context)
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        math = _mako_get_namespace(context, 'math')
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer('<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('" itemscope="itemscope" itemtype="http://schema.org/Article">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <p class="dateline"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark"><i class="fa fa-clock"></i> <time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time></a></p>\n            <p class="byline author vcard"> <i class="fa fa-user"></i> <span class="byline-name fn" itemprop="author">\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('            </span></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline"><i class="fa fa-comment"></i> ')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('    </div>\n    </article>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content_header():
            return render_content_header(context)
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/zen/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "35": 6, "41": 0, "76": 2, "77": 3, "78": 4, "79": 5, "80": 6, "81": 7, "86": 15, "91": 60, "97": 9, "110": 9, "111": 10, "112": 10, "113": 11, "114": 12, "115": 12, "116": 12, "117": 14, "118": 14, "119": 14, "125": 17, "154": 17, "159": 20, "160": 21, "161": 22, "162": 22, "163": 22, "164": 24, "165": 25, "166": 25, "167": 25, "168": 27, "169": 28, "170": 29, "171": 29, "172": 29, "173": 31, "174": 31, "175": 31, "176": 31, "177": 33, "178": 33, "179": 33, "180": 33, "181": 33, "182": 33, "183": 33, "184": 33, "185": 35, "186": 36, "187": 36, "188": 36, "189": 36, "190": 36, "191": 37, "192": 38, "193": 38, "194": 38, "195": 40, "196": 41, "197": 42, "198": 42, "199": 42, "200": 44, "201": 46, "202": 47, "203": 48, "204": 48, "205": 49, "206": 50, "207": 51, "208": 51, "209": 53, "210": 56, "211": 57, "212": 57, "213": 58, "214": 58, "215": 59, "216": 59, "222": 18, "232": 18, "233": 19, "234": 19, "240": 234}}
__M_END_METADATA
"""
