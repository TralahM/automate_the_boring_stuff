# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1564943191.40618
_enable_loop = True
_template_filename = 'themes/zen/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'late_load_js', 'html_stylesheets', 'html_feedlinks', 'html_translations', 'html_navigation_links']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def html_stylesheets():
            return render_html_stylesheets(context)
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        is_rtl = _import_ns.get('is_rtl', context.get('is_rtl', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        comment_system_id = _import_ns.get('comment_system_id', context.get('comment_system_id', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        favicons = _import_ns.get('favicons', context.get('favicons', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        theme_color = _import_ns.get('theme_color', context.get('theme_color', UNDEFINED))
        meta_generator_tag = _import_ns.get('meta_generator_tag', context.get('meta_generator_tag', UNDEFINED))
        url_type = _import_ns.get('url_type', context.get('url_type', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        url_replacer = _import_ns.get('url_replacer', context.get('url_replacer', UNDEFINED))
        comment_system = _import_ns.get('comment_system', context.get('comment_system', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("    prefix='")
        __M_writer('        og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('            fb: http://ogp.me/ns/fb# ')
        __M_writer("    ' ")
        __M_writer('    vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('    dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('        <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\n')
        if meta_generator_tag:
            __M_writer('        <meta name="generator" content="Nikola (getnikola.com)">\n')
        __M_writer('    ')
        __M_writer(str(feeds_translations.head(classification=None, kind='index', other=False)))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5shiv-printshiv.min.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        social_buttons_code = _import_ns.get('social_buttons_code', context.get('social_buttons_code', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.9.1/baguetteBox.min.js" integrity="sha256-SoEATAB7PgNWyyK100I7yQXYm5V08k5SFupDP0h72MY=" crossorigin="anonymous"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.9.1/baguetteBox.min.js" integrity="sha256-SoEATAB7PgNWyyK100I7yQXYm5V08k5SFupDP0h72MY=" crossorigin="anonymous"></script>\n            <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.1/moment-with-locales.min.js" integrity="sha256-ZykW30UBCXWkPGsVyVPdJlUrce9/PawgYCEzinA4pnU=" crossorigin="anonymous"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/baguetteBox.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        needs_ipython_css = _import_ns.get('needs_ipython_css', context.get('needs_ipython_css', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        has_custom_css = _import_ns.get('has_custom_css', context.get('has_custom_css', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <link href="https://fonts.googleapis.com/css?family=Bitter:400,400i,700" rel="stylesheet" type="text/css">\n    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.9.1/baguetteBox.min.css" integrity="sha256-GrjD69ygFQ+lWqlAOC6LzoNUE4jKrvgkQJrtIukHAi4=" crossorigin="anonymous" />\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('        <link href="/assets/css/baguetteBox.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/rst_base.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(classification=None, kind='index', other=False)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <ul class="translations">\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text, icon in navigation_links[lang]:
            if rel_link(permalink, url) == "#":
                __M_writer('            <li class="active"><a href="')
                __M_writer(str(permalink))
                __M_writer('" title="')
                __M_writer(str(text))
                __M_writer(' ')
                __M_writer(str(messages("(active)", lang)))
                __M_writer('"><i class="')
                __M_writer(str(icon))
                __M_writer('"></i></a></li>\n')
            else:
                __M_writer('            <li><a href="')
                __M_writer(str(url))
                __M_writer('" title="')
                __M_writer(str(text))
                __M_writer('"><i class="')
                __M_writer(str(icon))
                __M_writer('"></i></a></li>\n')
        __M_writer('    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/zen/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 63, "35": 82, "36": 108, "37": 113, "38": 123, "39": 135, "45": 4, "72": 4, "73": 7, "74": 8, "75": 9, "76": 10, "77": 12, "78": 13, "79": 14, "80": 15, "81": 18, "82": 18, "83": 18, "84": 21, "85": 22, "86": 22, "87": 22, "88": 24, "89": 25, "90": 26, "91": 26, "92": 26, "93": 27, "94": 28, "95": 28, "96": 28, "97": 28, "98": 28, "99": 30, "100": 31, "101": 31, "102": 32, "103": 32, "104": 33, "105": 34, "106": 36, "107": 36, "108": 36, "109": 37, "110": 37, "111": 39, "112": 40, "113": 41, "114": 41, "115": 41, "116": 41, "117": 41, "118": 41, "119": 41, "120": 44, "121": 45, "122": 46, "123": 46, "124": 46, "125": 48, "126": 49, "127": 50, "128": 50, "129": 50, "130": 52, "131": 53, "132": 53, "133": 53, "134": 55, "135": 56, "136": 57, "137": 58, "138": 59, "139": 59, "140": 59, "141": 61, "142": 62, "143": 62, "149": 65, "158": 65, "159": 66, "160": 67, "161": 68, "162": 69, "163": 70, "164": 72, "165": 73, "166": 74, "167": 76, "168": 77, "169": 81, "170": 81, "171": 81, "177": 84, "187": 84, "188": 87, "189": 88, "190": 89, "191": 91, "192": 92, "193": 94, "194": 95, "195": 100, "196": 101, "197": 104, "198": 105, "204": 111, "211": 111, "212": 112, "213": 112, "219": 115, "231": 115, "232": 117, "233": 118, "234": 119, "235": 119, "236": 119, "237": 119, "238": 119, "239": 119, "240": 119, "241": 122, "247": 125, "259": 125, "260": 126, "261": 127, "262": 128, "263": 128, "264": 128, "265": 128, "266": 128, "267": 128, "268": 128, "269": 128, "270": 128, "271": 129, "272": 130, "273": 130, "274": 130, "275": 130, "276": 130, "277": 130, "278": 130, "279": 133, "280": 133, "281": 133, "282": 134, "283": 134, "289": 283}}
__M_END_METADATA
"""
