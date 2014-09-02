# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1409626143.4046378
_enable_loop = True
_template_filename = '/home/mapologo/.virtualenvs/map0logo.github.io/lib/python3.4/site-packages/nikola/data/themes/bootstrap3/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'extra_head', 'content', 'belowtitle', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('notes', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'notes')] = ns

    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        show_sourcelink = _import_ns.get('show_sourcelink', context.get('show_sourcelink', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        notes = _mako_get_namespace(context, 'notes')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body>\n\n<!-- Menubar -->\n\n<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n    <div class="container"><!-- This keeps the margins nice -->\n        <div class="navbar-header">\n            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="')
        __M_writer(str(abs_link('/')))
        __M_writer('">\n')
        if logo_url:
            __M_writer('                <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(str(blog_title))
            __M_writer('" id="logo">\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('                <span id="blog-title">')
            __M_writer(str(blog_title))
            __M_writer('</span>\n')
        __M_writer('            </a>\n        </div><!-- /.navbar-header -->\n        <div class="collapse navbar-collapse navbar-ex1-collapse">\n            <ul class="nav navbar-nav">\n                ')
        __M_writer(str(base.html_navigation_links()))
        __M_writer('\n                ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n            </ul>\n')
        if search_form:
            __M_writer('                ')
            __M_writer(str(search_form))
            __M_writer('\n')
        __M_writer('\n            <ul class="nav navbar-nav navbar-right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer('\n')
        if show_sourcelink:
            __M_writer('                    ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            __M_writer('\n')
        __M_writer('                ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n            </ul>\n        </div><!-- /.navbar-collapse -->\n    </div><!-- /.container -->\n</nav>\n\n<!-- End of Menubar -->\n\n<div class="container">\n    <div class="body-content">\n        <!--Body content-->\n        <div class="row">\n            ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </div>\n        <!--End of body content-->\n\n        <footer>\n            ')
        __M_writer(str(content_footer))
        __M_writer('\n            ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n        </footer>\n    </div>\n</div>\n\n')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n    <script>jQuery("a.image-reference").colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer('        ')
            __M_writer(str(notes.code()))
            __M_writer('\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer('        ')
            __M_writer(str(notes.code()))
            __M_writer('\n')
        __M_writer(str(body_end))
        __M_writer('\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def belowtitle():
            return render_belowtitle(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('                    <li>')
            __M_writer(str(base.html_translations()))
            __M_writer('</li>\n')
        __M_writer('                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"192": 44, "131": 78, "132": 79, "133": 80, "134": 80, "135": 80, "136": 81, "137": 82, "138": 82, "139": 82, "140": 84, "141": 84, "142": 85, "143": 85, "205": 45, "149": 50, "22": 3, "25": 2, "28": 0, "163": 6, "207": 46, "172": 6, "206": 46, "178": 65, "209": 48, "215": 78, "63": 2, "64": 3, "65": 4, "66": 4, "67": 5, "68": 5, "73": 8, "74": 9, "75": 9, "76": 24, "77": 24, "78": 25, "79": 26, "80": 26, "81": 26, "82": 26, "83": 26, "84": 28, "85": 29, "86": 30, "87": 30, "88": 30, "89": 32, "90": 36, "91": 36, "92": 37, "93": 37, "94": 39, "95": 40, "96": 40, "97": 40, "98": 42, "229": 215, "103": 48, "104": 49, "105": 50, "208": 46, "110": 50, "111": 52, "112": 52, "113": 52, "114": 64, "115": 64, "204": 44, "120": 65, "121": 70, "122": 70, "123": 71, "124": 71, "125": 76, "126": 76}, "source_encoding": "utf-8", "filename": "/home/mapologo/.virtualenvs/map0logo.github.io/lib/python3.4/site-packages/nikola/data/themes/bootstrap3/templates/base.tmpl", "uri": "base.tmpl"}
__M_END_METADATA
"""
