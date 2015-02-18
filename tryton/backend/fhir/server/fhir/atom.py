from .base_classes import *
from .support_functions import *

class DateTimeType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, base=None, valueOf_=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.base = _cast(None, base)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if DateTimeType.subclass:
            return DateTimeType.subclass(*args_, **kwargs_)
        else:
            return DateTimeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_base(self): return self.base
    def set_base(self, base): self.base = base
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
        ):
            return True
        else:
            return False
    @staticmethod
    def format_iso8601(obj):
        """Format a datetime object for iso8601 (Atom standard)"""
        iso8601 = obj.isoformat()
        if obj.tzinfo:
            return iso8601
        return ''.join((iso8601,'Z'))
    def export(self, outfile, level, namespace_='', name_='DateTimeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DateTimeType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.format_iso8601(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DateTimeType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DateTimeType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            outfile.write(' base=%s' % (self.gds_format_string(quote_attrib(self.base).encode(ExternalEncoding), input_name='base'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='DateTimeType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='DateTimeType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            showIndent(outfile, level)
            outfile.write('lang="%s",\n' % (self.lang,))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            showIndent(outfile, level)
            outfile.write('base="%s",\n' % (self.base,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
        value = find_attr_value_('base', node)
        if value is not None and 'base' not in already_processed:
            already_processed.add('base')
            self.base = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass

class deleted_entry(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, when=None, ref=None, link=None):
        self.original_tagname_ = None
        if isinstance(when, basestring):
            initvalue_ = datetime_.datetime.strptime(when, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = when
        self.when = initvalue_
        self.ref = _cast(None, ref)
        self.link = link
    def factory(*args_, **kwargs_):
        if deleted_entry.subclass:
            return deleted_entry.subclass(*args_, **kwargs_)
        else:
            return deleted_entry(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_link(self): return self.link
    def set_link(self, link): self.link = link
    def get_when(self): return self.when
    def set_when(self, when): self.when = when
    def get_ref(self): return self.ref
    def set_ref(self, ref): self.ref = ref
    def hasContent_(self):
        if (
            self.link is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='deleted-entry', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='deleted-entry')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='deleted-entry', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='deleted-entry'):
        if self.when is not None and 'when' not in already_processed:
            already_processed.add('when')
            outfile.write(' when="%s"' % self.gds_format_datetime(self.when, input_name='when'))
        if self.ref is not None and 'ref' not in already_processed:
            already_processed.add('ref')
            outfile.write(' ref=%s' % (self.gds_format_string(quote_attrib(self.ref).encode(ExternalEncoding), input_name='ref'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='deleted-entry', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.link is not None:
            self.link.export(outfile, level, namespace_, name_='link', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='deleted-entry'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.when is not None and 'when' not in already_processed:
            already_processed.add('when')
            showIndent(outfile, level)
            outfile.write('when=model_.GeneratedsSuper.gds_parse_datetime("%s"),\n' % self.gds_format_datetime(self.when, input_name='when'))
        if self.ref is not None and 'ref' not in already_processed:
            already_processed.add('ref')
            showIndent(outfile, level)
            outfile.write('ref="%s",\n' % (self.ref,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.link is not None:
            showIndent(outfile, level)
            outfile.write('link=model_.linkType(\n')
            self.link.exportLiteral(outfile, level, name_='link')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('when', node)
        if value is not None and 'when' not in already_processed:
            already_processed.add('when')
            try:
                self.when = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (when): %s' % exp)
        value = find_attr_value_('ref', node)
        if value is not None and 'ref' not in already_processed:
            already_processed.add('ref')
            self.ref = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'link':
            obj_ = linkType.factory()
            obj_.build(child_)
            self.link = obj_
            obj_.original_tagname_ = 'link'

class PersonType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, base=None, name=None, uri=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.base = _cast(None, base)
        if name is None:
            self.name = []
        else:
            self.name = name
        if uri is None:
            self.uri = []
        else:
            self.uri = uri
    def factory(*args_, **kwargs_):
        if PersonType.subclass:
            return PersonType.subclass(*args_, **kwargs_)
        else:
            return PersonType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def add_name(self, value): self.name.append(value)
    def insert_name_at(self, index, value): self.name.insert(index, value)
    def replace_name_at(self, index, value): self.name[index] = value
    def get_uri(self): return self.uri
    def set_uri(self, uri): self.uri = uri
    def add_uri(self, value): self.uri.append(value)
    def insert_uri_at(self, index, value): self.uri.insert(index, value)
    def replace_uri_at(self, index, value): self.uri[index] = value
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_base(self): return self.base
    def set_base(self, base): self.base = base
    def hasContent_(self):
        if (
            self.name or
            self.uri
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='PersonType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PersonType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='PersonType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='PersonType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            outfile.write(' base=%s' % (self.gds_format_string(quote_attrib(self.base).encode(ExternalEncoding), input_name='base'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='PersonType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for name_ in self.name:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname>%s</%sname>%s' % (namespace_, self.gds_format_string(quote_xml(name_).encode(ExternalEncoding), input_name='name'), namespace_, eol_))
        for uri_ in self.uri:
            uri_.export(outfile, level, namespace_, name_='uri', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='PersonType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            showIndent(outfile, level)
            outfile.write('lang="%s",\n' % (self.lang,))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            showIndent(outfile, level)
            outfile.write('base="%s",\n' % (self.base,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('name=[\n')
        level += 1
        for name_ in self.name:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(name_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('uri=[\n')
        level += 1
        for uri_ in self.uri:
            showIndent(outfile, level)
            outfile.write('model_.UriType(\n')
            uri_.exportLiteral(outfile, level, name_='UriType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
        value = find_attr_value_('base', node)
        if value is not None and 'base' not in already_processed:
            already_processed.add('base')
            self.base = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'name':
            name_ = child_.text
            name_ = self.gds_validate_string(name_, node, 'name')
            self.name.append(name_)
        elif nodeName_ == 'uri':
            obj_ = UriType.factory()
            obj_.build(child_)
            self.uri.append(obj_)
            obj_.original_tagname_ = 'uri'

class FeedType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, base=None, title=None, updated=None, id=None, link=None, author=None, category=None, entry=None, deleted_entry=None, totalResults=None, score=None, Signature=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.base = _cast(None, base)
        if title is None:
            self.title = []
        else:
            self.title = title
        if updated is None:
            self.updated = []
        else:
            self.updated = updated
        if id is None:
            self.id = []
        else:
            self.id = id
        if link is None:
            self.link = []
        else:
            self.link = link
        if author is None:
            self.author = []
        else:
            self.author = author
        if category is None:
            self.category = []
        else:
            self.category = category
        if entry is None:
            self.entry = []
        else:
            self.entry = entry
        if deleted_entry is None:
            self.deleted_entry = []
        else:
            self.deleted_entry = deleted_entry
        if totalResults is None:
            self.totalResults = []
        else:
            self.totalResults = totalResults
        if score is None:
            self.score = []
        else:
            self.score = score
        self.Signature = Signature
    def factory(*args_, **kwargs_):
        if FeedType.subclass:
            return FeedType.subclass(*args_, **kwargs_)
        else:
            return FeedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def add_title(self, value): self.title.append(value)
    def insert_title_at(self, index, value): self.title.insert(index, value)
    def replace_title_at(self, index, value): self.title[index] = value
    def get_updated(self): return self.updated
    def set_updated(self, updated): self.updated = updated
    def add_updated(self, value): self.updated.append(value)
    def insert_updated_at(self, index, value): self.updated.insert(index, value)
    def replace_updated_at(self, index, value): self.updated[index] = value
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def add_id(self, value): self.id.append(value)
    def insert_id_at(self, index, value): self.id.insert(index, value)
    def replace_id_at(self, index, value): self.id[index] = value
    def get_link(self): return self.link
    def set_link(self, link): self.link = link
    def add_link(self, value): self.link.append(value)
    def insert_link_at(self, index, value): self.link.insert(index, value)
    def replace_link_at(self, index, value): self.link[index] = value
    def get_author(self): return self.author
    def set_author(self, author): self.author = author
    def add_author(self, value): self.author.append(value)
    def insert_author_at(self, index, value): self.author.insert(index, value)
    def replace_author_at(self, index, value): self.author[index] = value
    def get_category(self): return self.category
    def set_category(self, category): self.category = category
    def add_category(self, value): self.category.append(value)
    def insert_category_at(self, index, value): self.category.insert(index, value)
    def replace_category_at(self, index, value): self.category[index] = value
    def get_entry(self): return self.entry
    def set_entry(self, entry): self.entry = entry
    def add_entry(self, value): self.entry.append(value)
    def insert_entry_at(self, index, value): self.entry.insert(index, value)
    def replace_entry_at(self, index, value): self.entry[index] = value
    def get_deleted_entry(self): return self.deleted_entry
    def set_deleted_entry(self, deleted_entry): self.deleted_entry = deleted_entry
    def add_deleted_entry(self, value): self.deleted_entry.append(value)
    def insert_deleted_entry_at(self, index, value): self.deleted_entry.insert(index, value)
    def replace_deleted_entry_at(self, index, value): self.deleted_entry[index] = value
    def get_totalResults(self): return self.totalResults
    def set_totalResults(self, totalResults): self.totalResults = totalResults
    def add_totalResults(self, value): self.totalResults.append(value)
    def insert_totalResults_at(self, index, value): self.totalResults.insert(index, value)
    def replace_totalResults_at(self, index, value): self.totalResults[index] = value
    def get_score(self): return self.score
    def set_score(self, score): self.score = score
    def add_score(self, value): self.score.append(value)
    def insert_score_at(self, index, value): self.score.insert(index, value)
    def replace_score_at(self, index, value): self.score[index] = value
    def get_Signature(self): return self.Signature
    def set_Signature(self, Signature): self.Signature = Signature
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_base(self): return self.base
    def set_base(self, base): self.base = base
    def hasContent_(self):
        if (
            self.title or
            self.updated or
            self.id or
            self.link or
            self.author or
            self.category or
            self.entry or
            self.deleted_entry or
            self.totalResults or
            self.score or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='FeedType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        #only run once (hopefully)
        outfile.write('<?xml version="1.0" encoding="utf-8"?>\n')
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='FeedType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='FeedType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='FeedType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            outfile.write(' base=%s' % (self.gds_format_string(quote_attrib(self.base).encode(ExternalEncoding), input_name='base'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='FeedType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for title_ in self.title:
            title_.export(outfile, level, namespace_, name_='title', pretty_print=pretty_print)
        for updated_ in self.updated:
            updated_.export(outfile, level, namespace_, name_='updated', pretty_print=pretty_print)
        for id_ in self.id:
            id_.export(outfile, level, namespace_, name_='id', pretty_print=pretty_print)
        for link_ in self.link:
            link_.export(outfile, level, namespace_, name_='link', pretty_print=pretty_print)
        for author_ in self.author:
            author_.export(outfile, level, namespace_, name_='author', pretty_print=pretty_print)
        for category_ in self.category:
            category_.export(outfile, level, namespace_, name_='category', pretty_print=pretty_print)
        for entry_ in self.entry:
            entry_.export(outfile, level, namespace_, name_='entry', pretty_print=pretty_print)
        for deleted_entry_ in self.deleted_entry:
            deleted_entry_.export(outfile, level, namespace_='at:', name_='deleted-entry', pretty_print=pretty_print)
        for totalResults_ in self.totalResults:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stotalResults>%s</%stotalResults>%s' %
                        ('os:',
                        self.gds_format_integer(totalResults_,
                                input_name='totalResults'),
                        'os:',
                        eol_))
        for score_ in self.score:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sscore>%s</%sscore>%s' % (namespace_, self.gds_format_float(score_, input_name='score'), namespace_, eol_))
        if self.Signature is not None:
            self.Signature.export(outfile, level, namespace_='ds:', name_='Signature', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='FeedType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            showIndent(outfile, level)
            outfile.write('lang="%s",\n' % (self.lang,))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            showIndent(outfile, level)
            outfile.write('base="%s",\n' % (self.base,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('title=[\n')
        level += 1
        for title_ in self.title:
            showIndent(outfile, level)
            outfile.write('model_.TextType(\n')
            title_.exportLiteral(outfile, level, name_='TextType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('updated=[\n')
        level += 1
        for updated_ in self.updated:
            showIndent(outfile, level)
            outfile.write('model_.DateTimeType(\n')
            updated_.exportLiteral(outfile, level, name_='DateTimeType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('id=[\n')
        level += 1
        for id_ in self.id:
            showIndent(outfile, level)
            outfile.write('model_.IdType(\n')
            id_.exportLiteral(outfile, level, name_='IdType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('link=[\n')
        level += 1
        for link_ in self.link:
            showIndent(outfile, level)
            outfile.write('model_.LinkType(\n')
            link_.exportLiteral(outfile, level, name_='LinkType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('author=[\n')
        level += 1
        for author_ in self.author:
            showIndent(outfile, level)
            outfile.write('model_.PersonType(\n')
            author_.exportLiteral(outfile, level, name_='PersonType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('category=[\n')
        level += 1
        for category_ in self.category:
            showIndent(outfile, level)
            outfile.write('model_.CategoryType(\n')
            category_.exportLiteral(outfile, level, name_='CategoryType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('entry=[\n')
        level += 1
        for entry_ in self.entry:
            showIndent(outfile, level)
            outfile.write('model_.EntryType(\n')
            entry_.exportLiteral(outfile, level, name_='EntryType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('deleted_entry=[\n')
        level += 1
        for deleted_entry_ in self.deleted_entry:
            showIndent(outfile, level)
            outfile.write('model_.deleted_entry(\n')
            deleted_entry_.exportLiteral(outfile, level, name_='deleted-entry')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('totalResults=[\n')
        level += 1
        for totalResults_ in self.totalResults:
            showIndent(outfile, level)
            outfile.write('%d,\n' % totalResults_)
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('score=[\n')
        level += 1
        for score_ in self.score:
            showIndent(outfile, level)
            outfile.write('%f,\n' % score_)
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Signature is not None:
            showIndent(outfile, level)
            outfile.write('Signature=model_.Signature(\n')
            self.Signature.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
        value = find_attr_value_('base', node)
        if value is not None and 'base' not in already_processed:
            already_processed.add('base')
            self.base = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'title':
            obj_ = TextType.factory()
            obj_.build(child_)
            self.title.append(obj_)
            obj_.original_tagname_ = 'title'
        elif nodeName_ == 'updated':
            obj_ = DateTimeType.factory()
            obj_.build(child_)
            self.updated.append(obj_)
            obj_.original_tagname_ = 'updated'
        elif nodeName_ == 'id':
            obj_ = IdType.factory()
            obj_.build(child_)
            self.id.append(obj_)
            obj_.original_tagname_ = 'id'
        elif nodeName_ == 'link':
            obj_ = LinkType.factory()
            obj_.build(child_)
            self.link.append(obj_)
            obj_.original_tagname_ = 'link'
        elif nodeName_ == 'author':
            obj_ = PersonType.factory()
            obj_.build(child_)
            self.author.append(obj_)
            obj_.original_tagname_ = 'author'
        elif nodeName_ == 'category':
            obj_ = CategoryType.factory()
            obj_.build(child_)
            self.category.append(obj_)
            obj_.original_tagname_ = 'category'
        elif nodeName_ == 'entry':
            obj_ = EntryType.factory()
            obj_.build(child_)
            self.entry.append(obj_)
            obj_.original_tagname_ = 'entry'
        elif nodeName_ == 'deleted-entry':
            obj_ = deleted_entry.factory()
            obj_.build(child_)
            self.deleted_entry.append(obj_)
            obj_.original_tagname_ = 'deleted-entry'
        elif nodeName_ == 'totalResults':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError) as exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'totalResults')
            self.totalResults.append(ival_)
        elif nodeName_ == 'score':
            sval_ = child_.text
            try:
                fval_ = float(sval_)
            except (TypeError, ValueError) as exp:
                raise_parse_error(child_, 'requires float or double: %s' % exp)
            fval_ = self.gds_validate_float(fval_, node, 'score')
            self.score.append(fval_)
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory()
            obj_.build(child_)
            self.Signature = obj_
            obj_.original_tagname_ = 'Signature'

class EntryType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, base=None, title=None, link=None, id=None, updated=None, published=None, author=None, category=None, content=None, summary=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.base = _cast(None, base)
        if title is None:
            self.title = []
        else:
            self.title = title
        if link is None:
            self.link = []
        else:
            self.link = link
        if id is None:
            self.id = []
        else:
            self.id = id
        if updated is None:
            self.updated = []
        else:
            self.updated = updated
        if published is None:
            self.published = []
        else:
            self.published = published
        if author is None:
            self.author = []
        else:
            self.author = author
        if category is None:
            self.category = []
        else:
            self.category = category
        if content is None:
            self.content = []
        else:
            self.content = content
        if summary is None:
            self.summary = []
        else:
            self.summary = summary
    def factory(*args_, **kwargs_):
        if EntryType.subclass:
            return EntryType.subclass(*args_, **kwargs_)
        else:
            return EntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def add_title(self, value): self.title.append(value)
    def insert_title_at(self, index, value): self.title.insert(index, value)
    def replace_title_at(self, index, value): self.title[index] = value
    def get_link(self): return self.link
    def set_link(self, link): self.link = link
    def add_link(self, value): self.link.append(value)
    def insert_link_at(self, index, value): self.link.insert(index, value)
    def replace_link_at(self, index, value): self.link[index] = value
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def add_id(self, value): self.id.append(value)
    def insert_id_at(self, index, value): self.id.insert(index, value)
    def replace_id_at(self, index, value): self.id[index] = value
    def get_updated(self): return self.updated
    def set_updated(self, updated): self.updated = updated
    def add_updated(self, value): self.updated.append(value)
    def insert_updated_at(self, index, value): self.updated.insert(index, value)
    def replace_updated_at(self, index, value): self.updated[index] = value
    def get_published(self): return self.published
    def set_published(self, published): self.published = published
    def add_published(self, value): self.published.append(value)
    def insert_published_at(self, index, value): self.published.insert(index, value)
    def replace_published_at(self, index, value): self.published[index] = value
    def get_author(self): return self.author
    def set_author(self, author): self.author = author
    def add_author(self, value): self.author.append(value)
    def insert_author_at(self, index, value): self.author.insert(index, value)
    def replace_author_at(self, index, value): self.author[index] = value
    def get_category(self): return self.category
    def set_category(self, category): self.category = category
    def add_category(self, value): self.category.append(value)
    def insert_category_at(self, index, value): self.category.insert(index, value)
    def replace_category_at(self, index, value): self.category[index] = value
    def get_content(self): return self.content
    def set_content(self, content): self.content = content
    def add_content(self, value): self.content.append(value)
    def insert_content_at(self, index, value): self.content.insert(index, value)
    def replace_content_at(self, index, value): self.content[index] = value
    def get_summary(self): return self.summary
    def set_summary(self, summary): self.summary = summary
    def add_summary(self, value): self.summary.append(value)
    def insert_summary_at(self, index, value): self.summary.insert(index, value)
    def replace_summary_at(self, index, value): self.summary[index] = value
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_base(self): return self.base
    def set_base(self, base): self.base = base
    def validate_ContentType(self, value):
        # Validate type ContentType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_:
            pass
    def hasContent_(self):
        if (
            self.title or
            self.link or
            self.id or
            self.updated or
            self.published or
            self.author or
            self.category or
            self.content or
            self.summary
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='EntryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='EntryType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='EntryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='EntryType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            outfile.write(' base=%s' % (self.gds_format_string(quote_attrib(self.base).encode(ExternalEncoding), input_name='base'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='EntryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for title_ in self.title:
            title_.export(outfile, level, namespace_, name_='title', pretty_print=pretty_print)
        for link_ in self.link:
            link_.export(outfile, level, namespace_, name_='link', pretty_print=pretty_print)
        for id_ in self.id:
            id_.export(outfile, level, namespace_, name_='id', pretty_print=pretty_print)
        for updated_ in self.updated:
            updated_.export(outfile, level, namespace_, name_='updated', pretty_print=pretty_print)
        for published_ in self.published:
            published_.export(outfile, level, namespace_, name_='published', pretty_print=pretty_print)
        for author_ in self.author:
            author_.export(outfile, level, namespace_, name_='author', pretty_print=pretty_print)
        for category_ in self.category:
            category_.export(outfile, level, namespace_, name_='category', pretty_print=pretty_print)
        for content_ in self.content:
            content_.export(outfile, level, namespace_, name_='content', pretty_print=pretty_print)
        for summary_ in self.summary:
            summary_.export(outfile, level, namespace_, name_='summary', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='EntryType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            showIndent(outfile, level)
            outfile.write('lang="%s",\n' % (self.lang,))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            showIndent(outfile, level)
            outfile.write('base="%s",\n' % (self.base,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('title=[\n')
        level += 1
        for title_ in self.title:
            showIndent(outfile, level)
            outfile.write('model_.TextType(\n')
            title_.exportLiteral(outfile, level, name_='TextType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('link=[\n')
        level += 1
        for link_ in self.link:
            showIndent(outfile, level)
            outfile.write('model_.LinkType(\n')
            link_.exportLiteral(outfile, level, name_='LinkType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('id=[\n')
        level += 1
        for id_ in self.id:
            showIndent(outfile, level)
            outfile.write('model_.IdType(\n')
            id_.exportLiteral(outfile, level, name_='IdType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('updated=[\n')
        level += 1
        for updated_ in self.updated:
            showIndent(outfile, level)
            outfile.write('model_.DateTimeType(\n')
            updated_.exportLiteral(outfile, level, name_='DateTimeType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('published=[\n')
        level += 1
        for published_ in self.published:
            showIndent(outfile, level)
            outfile.write('model_.DateTimeType(\n')
            published_.exportLiteral(outfile, level, name_='DateTimeType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('author=[\n')
        level += 1
        for author_ in self.author:
            showIndent(outfile, level)
            outfile.write('model_.PersonType(\n')
            author_.exportLiteral(outfile, level, name_='PersonType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('category=[\n')
        level += 1
        for category_ in self.category:
            showIndent(outfile, level)
            outfile.write('model_.CategoryType(\n')
            category_.exportLiteral(outfile, level, name_='CategoryType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('content=[\n')
        level += 1
        for content_ in self.content:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(content_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('summary=[\n')
        level += 1
        for summary_ in self.summary:
            showIndent(outfile, level)
            outfile.write('model_.TextType(\n')
            summary_.exportLiteral(outfile, level, name_='TextType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
        value = find_attr_value_('base', node)
        if value is not None and 'base' not in already_processed:
            already_processed.add('base')
            self.base = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'title':
            obj_ = TextType.factory()
            obj_.build(child_)
            self.title.append(obj_)
            obj_.original_tagname_ = 'title'
        elif nodeName_ == 'link':
            obj_ = LinkType.factory()
            obj_.build(child_)
            self.link.append(obj_)
            obj_.original_tagname_ = 'link'
        elif nodeName_ == 'id':
            obj_ = IdType.factory()
            obj_.build(child_)
            self.id.append(obj_)
            obj_.original_tagname_ = 'id'
        elif nodeName_ == 'updated':
            obj_ = DateTimeType.factory()
            obj_.build(child_)
            self.updated.append(obj_)
            obj_.original_tagname_ = 'updated'
        elif nodeName_ == 'published':
            obj_ = DateTimeType.factory()
            obj_.build(child_)
            self.published.append(obj_)
            obj_.original_tagname_ = 'published'
        elif nodeName_ == 'author':
            obj_ = PersonType.factory()
            obj_.build(child_)
            self.author.append(obj_)
            obj_.original_tagname_ = 'author'
        elif nodeName_ == 'category':
            obj_ = CategoryType.factory()
            obj_.build(child_)
            self.category.append(obj_)
            obj_.original_tagname_ = 'category'
        elif nodeName_ == 'content':
            obj_ = ContentType.factory()
            obj_.build(child_)
            self.content.append(obj_)
            obj_.original_tagname_ = 'content'
        elif nodeName_ == 'summary':
            obj_ = TextType.factory()
            obj_.build(child_)
            self.summary.append(obj_)
            obj_.original_tagname_ = 'summary'

class CategoryType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, term=None, scheme=None, base=None, label=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.term = _cast(None, term)
        self.scheme = _cast(None, scheme)
        self.base = _cast(None, base)
        self.label = _cast(None, label)
    def factory(*args_, **kwargs_):
        if CategoryType.subclass:
            return CategoryType.subclass(*args_, **kwargs_)
        else:
            return CategoryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_term(self): return self.term
    def set_term(self, term): self.term = term
    def get_scheme(self): return self.scheme
    def set_scheme(self, scheme): self.scheme = scheme
    def get_base(self): return self.base
    def set_base(self, base): self.base = base
    def get_label(self): return self.label
    def set_label(self, label): self.label = label
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CategoryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CategoryType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CategoryType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CategoryType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.term is not None and 'term' not in already_processed:
            already_processed.add('term')
            outfile.write(' term=%s' % (self.gds_format_string(quote_attrib(self.term).encode(ExternalEncoding), input_name='term'), ))
        if self.scheme is not None and 'scheme' not in already_processed:
            already_processed.add('scheme')
            outfile.write(' scheme=%s' % (self.gds_format_string(quote_attrib(self.scheme).encode(ExternalEncoding), input_name='scheme'), ))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            outfile.write(' base=%s' % (self.gds_format_string(quote_attrib(self.base).encode(ExternalEncoding), input_name='base'), ))
        if self.label is not None and 'label' not in already_processed:
            already_processed.add('label')
            outfile.write(' label=%s' % (self.gds_format_string(quote_attrib(self.label).encode(ExternalEncoding), input_name='label'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='CategoryType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='CategoryType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            showIndent(outfile, level)
            outfile.write('lang="%s",\n' % (self.lang,))
        if self.term is not None and 'term' not in already_processed:
            already_processed.add('term')
            showIndent(outfile, level)
            outfile.write('term="%s",\n' % (self.term,))
        if self.scheme is not None and 'scheme' not in already_processed:
            already_processed.add('scheme')
            showIndent(outfile, level)
            outfile.write('scheme="%s",\n' % (self.scheme,))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            showIndent(outfile, level)
            outfile.write('base="%s",\n' % (self.base,))
        if self.label is not None and 'label' not in already_processed:
            already_processed.add('label')
            showIndent(outfile, level)
            outfile.write('label="%s",\n' % (self.label,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
        value = find_attr_value_('term', node)
        if value is not None and 'term' not in already_processed:
            already_processed.add('term')
            self.term = value
        value = find_attr_value_('scheme', node)
        if value is not None and 'scheme' not in already_processed:
            already_processed.add('scheme')
            self.scheme = value
        value = find_attr_value_('base', node)
        if value is not None and 'base' not in already_processed:
            already_processed.add('base')
            self.base = value
        value = find_attr_value_('label', node)
        if value is not None and 'label' not in already_processed:
            already_processed.add('label')
            self.label = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass

class ContentType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, base=None, type_=None, Binary=None, feed=None, AdverseReaction=None, Alert=None, AllergyIntolerance=None, CarePlan=None, Composition=None, ConceptMap=None, Condition=None, Conformance=None, Device=None, DeviceObservationReport=None, DiagnosticOrder=None, DiagnosticReport=None, DocumentManifest=None, DocumentReference=None, Encounter=None, FamilyHistory=None, Group=None, ImagingStudy=None, Immunization=None, ImmunizationRecommendation=None, List=None, Location=None, Media=None, Medication=None, MedicationAdministration=None, MedicationDispense=None, MedicationPrescription=None, MedicationStatement=None, MessageHeader=None, Observation=None, OperationOutcome=None, Order=None, OrderResponse=None, Organization=None, Other=None, Patient=None, Practitioner=None, Procedure=None, Profile=None, Provenance=None, Query=None, Questionnaire=None, RelatedPerson=None, SecurityEvent=None, Specimen=None, Substance=None, Supply=None, ValueSet=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.base = _cast(None, base)
        self.type_ = _cast(None, type_)
        self.Binary = Binary
        self.feed = feed
        self.AdverseReaction = AdverseReaction
        self.Alert = Alert
        self.AllergyIntolerance = AllergyIntolerance
        self.CarePlan = CarePlan
        self.Composition = Composition
        self.ConceptMap = ConceptMap
        self.Condition = Condition
        self.Conformance = Conformance
        self.Device = Device
        self.DeviceObservationReport = DeviceObservationReport
        self.DiagnosticOrder = DiagnosticOrder
        self.DiagnosticReport = DiagnosticReport
        self.DocumentManifest = DocumentManifest
        self.DocumentReference = DocumentReference
        self.Encounter = Encounter
        self.FamilyHistory = FamilyHistory
        self.Group = Group
        self.ImagingStudy = ImagingStudy
        self.Immunization = Immunization
        self.ImmunizationRecommendation = ImmunizationRecommendation
        self.List = List
        self.Location = Location
        self.Media = Media
        self.Medication = Medication
        self.MedicationAdministration = MedicationAdministration
        self.MedicationDispense = MedicationDispense
        self.MedicationPrescription = MedicationPrescription
        self.MedicationStatement = MedicationStatement
        self.MessageHeader = MessageHeader
        self.Observation = Observation
        self.OperationOutcome = OperationOutcome
        self.Order = Order
        self.OrderResponse = OrderResponse
        self.Organization = Organization
        self.Other = Other
        self.Patient = Patient
        self.Practitioner = Practitioner
        self.Procedure = Procedure
        self.Profile = Profile
        self.Provenance = Provenance
        self.Query = Query
        self.Questionnaire = Questionnaire
        self.RelatedPerson = RelatedPerson
        self.SecurityEvent = SecurityEvent
        self.Specimen = Specimen
        self.Substance = Substance
        self.Supply = Supply
        self.ValueSet = ValueSet
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ContentType.subclass:
            return ContentType.subclass(*args_, **kwargs_)
        else:
            return ContentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Binary(self): return self.Binary
    def set_Binary(self, Binary): self.Binary = Binary
    def get_feed(self): return self.feed
    def set_feed(self, feed): self.feed = feed
    def get_AdverseReaction(self): return self.AdverseReaction
    def set_AdverseReaction(self, AdverseReaction): self.AdverseReaction = AdverseReaction
    def get_Alert(self): return self.Alert
    def set_Alert(self, Alert): self.Alert = Alert
    def get_AllergyIntolerance(self): return self.AllergyIntolerance
    def set_AllergyIntolerance(self, AllergyIntolerance): self.AllergyIntolerance = AllergyIntolerance
    def get_CarePlan(self): return self.CarePlan
    def set_CarePlan(self, CarePlan): self.CarePlan = CarePlan
    def get_Composition(self): return self.Composition
    def set_Composition(self, Composition): self.Composition = Composition
    def get_ConceptMap(self): return self.ConceptMap
    def set_ConceptMap(self, ConceptMap): self.ConceptMap = ConceptMap
    def get_Condition(self): return self.Condition
    def set_Condition(self, Condition): self.Condition = Condition
    def get_Conformance(self): return self.Conformance
    def set_Conformance(self, Conformance): self.Conformance = Conformance
    def get_Device(self): return self.Device
    def set_Device(self, Device): self.Device = Device
    def get_DeviceObservationReport(self): return self.DeviceObservationReport
    def set_DeviceObservationReport(self, DeviceObservationReport): self.DeviceObservationReport = DeviceObservationReport
    def get_DiagnosticOrder(self): return self.DiagnosticOrder
    def set_DiagnosticOrder(self, DiagnosticOrder): self.DiagnosticOrder = DiagnosticOrder
    def get_DiagnosticReport(self): return self.DiagnosticReport
    def set_DiagnosticReport(self, DiagnosticReport): self.DiagnosticReport = DiagnosticReport
    def get_DocumentManifest(self): return self.DocumentManifest
    def set_DocumentManifest(self, DocumentManifest): self.DocumentManifest = DocumentManifest
    def get_DocumentReference(self): return self.DocumentReference
    def set_DocumentReference(self, DocumentReference): self.DocumentReference = DocumentReference
    def get_Encounter(self): return self.Encounter
    def set_Encounter(self, Encounter): self.Encounter = Encounter
    def get_FamilyHistory(self): return self.FamilyHistory
    def set_FamilyHistory(self, FamilyHistory): self.FamilyHistory = FamilyHistory
    def get_Group(self): return self.Group
    def set_Group(self, Group): self.Group = Group
    def get_ImagingStudy(self): return self.ImagingStudy
    def set_ImagingStudy(self, ImagingStudy): self.ImagingStudy = ImagingStudy
    def get_Immunization(self): return self.Immunization
    def set_Immunization(self, Immunization): self.Immunization = Immunization
    def get_ImmunizationRecommendation(self): return self.ImmunizationRecommendation
    def set_ImmunizationRecommendation(self, ImmunizationRecommendation): self.ImmunizationRecommendation = ImmunizationRecommendation
    def get_List(self): return self.List
    def set_List(self, List): self.List = List
    def get_Location(self): return self.Location
    def set_Location(self, Location): self.Location = Location
    def get_Media(self): return self.Media
    def set_Media(self, Media): self.Media = Media
    def get_Medication(self): return self.Medication
    def set_Medication(self, Medication): self.Medication = Medication
    def get_MedicationAdministration(self): return self.MedicationAdministration
    def set_MedicationAdministration(self, MedicationAdministration): self.MedicationAdministration = MedicationAdministration
    def get_MedicationDispense(self): return self.MedicationDispense
    def set_MedicationDispense(self, MedicationDispense): self.MedicationDispense = MedicationDispense
    def get_MedicationPrescription(self): return self.MedicationPrescription
    def set_MedicationPrescription(self, MedicationPrescription): self.MedicationPrescription = MedicationPrescription
    def get_MedicationStatement(self): return self.MedicationStatement
    def set_MedicationStatement(self, MedicationStatement): self.MedicationStatement = MedicationStatement
    def get_MessageHeader(self): return self.MessageHeader
    def set_MessageHeader(self, MessageHeader): self.MessageHeader = MessageHeader
    def get_Observation(self): return self.Observation
    def set_Observation(self, Observation): self.Observation = Observation
    def get_OperationOutcome(self): return self.OperationOutcome
    def set_OperationOutcome(self, OperationOutcome): self.OperationOutcome = OperationOutcome
    def get_Order(self): return self.Order
    def set_Order(self, Order): self.Order = Order
    def get_OrderResponse(self): return self.OrderResponse
    def set_OrderResponse(self, OrderResponse): self.OrderResponse = OrderResponse
    def get_Organization(self): return self.Organization
    def set_Organization(self, Organization): self.Organization = Organization
    def get_Other(self): return self.Other
    def set_Other(self, Other): self.Other = Other
    def get_Patient(self): return self.Patient
    def set_Patient(self, Patient): self.Patient = Patient
    def get_Practitioner(self): return self.Practitioner
    def set_Practitioner(self, Practitioner): self.Practitioner = Practitioner
    def get_Procedure(self): return self.Procedure
    def set_Procedure(self, Procedure): self.Procedure = Procedure
    def get_Profile(self): return self.Profile
    def set_Profile(self, Profile): self.Profile = Profile
    def get_Provenance(self): return self.Provenance
    def set_Provenance(self, Provenance): self.Provenance = Provenance
    def get_Query(self): return self.Query
    def set_Query(self, Query): self.Query = Query
    def get_Questionnaire(self): return self.Questionnaire
    def set_Questionnaire(self, Questionnaire): self.Questionnaire = Questionnaire
    def get_RelatedPerson(self): return self.RelatedPerson
    def set_RelatedPerson(self, RelatedPerson): self.RelatedPerson = RelatedPerson
    def get_SecurityEvent(self): return self.SecurityEvent
    def set_SecurityEvent(self, SecurityEvent): self.SecurityEvent = SecurityEvent
    def get_Specimen(self): return self.Specimen
    def set_Specimen(self, Specimen): self.Specimen = Specimen
    def get_Substance(self): return self.Substance
    def set_Substance(self, Substance): self.Substance = Substance
    def get_Supply(self): return self.Supply
    def set_Supply(self, Supply): self.Supply = Supply
    def get_ValueSet(self): return self.ValueSet
    def set_ValueSet(self, ValueSet): self.ValueSet = ValueSet
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_base(self): return self.base
    def set_base(self, base): self.base = base
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.Binary is not None or
            self.feed is not None or
            self.AdverseReaction is not None or
            self.Alert is not None or
            self.AllergyIntolerance is not None or
            self.CarePlan is not None or
            self.Composition is not None or
            self.ConceptMap is not None or
            self.Condition is not None or
            self.Conformance is not None or
            self.Device is not None or
            self.DeviceObservationReport is not None or
            self.DiagnosticOrder is not None or
            self.DiagnosticReport is not None or
            self.DocumentManifest is not None or
            self.DocumentReference is not None or
            self.Encounter is not None or
            self.FamilyHistory is not None or
            self.Group is not None or
            self.ImagingStudy is not None or
            self.Immunization is not None or
            self.ImmunizationRecommendation is not None or
            self.List is not None or
            self.Location is not None or
            self.Media is not None or
            self.Medication is not None or
            self.MedicationAdministration is not None or
            self.MedicationDispense is not None or
            self.MedicationPrescription is not None or
            self.MedicationStatement is not None or
            self.MessageHeader is not None or
            self.Observation is not None or
            self.OperationOutcome is not None or
            self.Order is not None or
            self.OrderResponse is not None or
            self.Organization is not None or
            self.Other is not None or
            self.Patient is not None or
            self.Practitioner is not None or
            self.Procedure is not None or
            self.Profile is not None or
            self.Provenance is not None or
            self.Query is not None or
            self.Questionnaire is not None or
            self.RelatedPerson is not None or
            self.SecurityEvent is not None or
            self.Specimen is not None or
            self.Substance is not None or
            self.Supply is not None or
            self.ValueSet is not None or
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ContentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, (' ' + namespacedef_ or '').rstrip(), ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ContentType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ContentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ContentType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            outfile.write(' base=%s' % (self.gds_format_string(quote_attrib(self.base).encode(ExternalEncoding), input_name='base'), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_format_string(quote_attrib(self.type_).encode(ExternalEncoding), input_name='type'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ContentType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ContentType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            showIndent(outfile, level)
            outfile.write('lang="%s",\n' % (self.lang,))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            showIndent(outfile, level)
            outfile.write('base="%s",\n' % (self.base,))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            showIndent(outfile, level)
            outfile.write('type_="%s",\n' % (self.type_,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
        value = find_attr_value_('base', node)
        if value is not None and 'base' not in already_processed:
            already_processed.add('base')
            self.base = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Binary':
            obj_ = Binary.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Binary', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Binary'):
              self.add_Binary(obj_.value)
            elif hasattr(self, 'set_Binary'):
              self.set_Binary(obj_.value)
        elif nodeName_ == 'feed':
            obj_ = feed.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'feed', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_feed'):
              self.add_feed(obj_.value)
            elif hasattr(self, 'set_feed'):
              self.set_feed(obj_.value)
        elif nodeName_ == 'AdverseReaction':
            obj_ = AdverseReaction.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'AdverseReaction', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_AdverseReaction'):
              self.add_AdverseReaction(obj_.value)
            elif hasattr(self, 'set_AdverseReaction'):
              self.set_AdverseReaction(obj_.value)
        elif nodeName_ == 'Alert':
            obj_ = Alert.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Alert', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Alert'):
              self.add_Alert(obj_.value)
            elif hasattr(self, 'set_Alert'):
              self.set_Alert(obj_.value)
        elif nodeName_ == 'AllergyIntolerance':
            obj_ = AllergyIntolerance.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'AllergyIntolerance', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_AllergyIntolerance'):
              self.add_AllergyIntolerance(obj_.value)
            elif hasattr(self, 'set_AllergyIntolerance'):
              self.set_AllergyIntolerance(obj_.value)
        elif nodeName_ == 'CarePlan':
            obj_ = CarePlan.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'CarePlan', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_CarePlan'):
              self.add_CarePlan(obj_.value)
            elif hasattr(self, 'set_CarePlan'):
              self.set_CarePlan(obj_.value)
        elif nodeName_ == 'Composition':
            obj_ = Composition.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Composition', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Composition'):
              self.add_Composition(obj_.value)
            elif hasattr(self, 'set_Composition'):
              self.set_Composition(obj_.value)
        elif nodeName_ == 'ConceptMap':
            obj_ = ConceptMap.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'ConceptMap', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_ConceptMap'):
              self.add_ConceptMap(obj_.value)
            elif hasattr(self, 'set_ConceptMap'):
              self.set_ConceptMap(obj_.value)
        elif nodeName_ == 'Condition':
            obj_ = Condition.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Condition', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Condition'):
              self.add_Condition(obj_.value)
            elif hasattr(self, 'set_Condition'):
              self.set_Condition(obj_.value)
        elif nodeName_ == 'Conformance':
            obj_ = Conformance.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Conformance', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Conformance'):
              self.add_Conformance(obj_.value)
            elif hasattr(self, 'set_Conformance'):
              self.set_Conformance(obj_.value)
        elif nodeName_ == 'Device':
            obj_ = Device.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Device', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Device'):
              self.add_Device(obj_.value)
            elif hasattr(self, 'set_Device'):
              self.set_Device(obj_.value)
        elif nodeName_ == 'DeviceObservationReport':
            obj_ = DeviceObservationReport.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'DeviceObservationReport', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_DeviceObservationReport'):
              self.add_DeviceObservationReport(obj_.value)
            elif hasattr(self, 'set_DeviceObservationReport'):
              self.set_DeviceObservationReport(obj_.value)
        elif nodeName_ == 'DiagnosticOrder':
            obj_ = DiagnosticOrder.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'DiagnosticOrder', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_DiagnosticOrder'):
              self.add_DiagnosticOrder(obj_.value)
            elif hasattr(self, 'set_DiagnosticOrder'):
              self.set_DiagnosticOrder(obj_.value)
        elif nodeName_ == 'DiagnosticReport':
            obj_ = DiagnosticReport.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'DiagnosticReport', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_DiagnosticReport'):
              self.add_DiagnosticReport(obj_.value)
            elif hasattr(self, 'set_DiagnosticReport'):
              self.set_DiagnosticReport(obj_.value)
        elif nodeName_ == 'DocumentManifest':
            obj_ = DocumentManifest.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'DocumentManifest', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_DocumentManifest'):
              self.add_DocumentManifest(obj_.value)
            elif hasattr(self, 'set_DocumentManifest'):
              self.set_DocumentManifest(obj_.value)
        elif nodeName_ == 'DocumentReference':
            obj_ = DocumentReference.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'DocumentReference', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_DocumentReference'):
              self.add_DocumentReference(obj_.value)
            elif hasattr(self, 'set_DocumentReference'):
              self.set_DocumentReference(obj_.value)
        elif nodeName_ == 'Encounter':
            obj_ = Encounter.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Encounter', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Encounter'):
              self.add_Encounter(obj_.value)
            elif hasattr(self, 'set_Encounter'):
              self.set_Encounter(obj_.value)
        elif nodeName_ == 'FamilyHistory':
            obj_ = FamilyHistory.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'FamilyHistory', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_FamilyHistory'):
              self.add_FamilyHistory(obj_.value)
            elif hasattr(self, 'set_FamilyHistory'):
              self.set_FamilyHistory(obj_.value)
        elif nodeName_ == 'Group':
            obj_ = Group.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Group', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Group'):
              self.add_Group(obj_.value)
            elif hasattr(self, 'set_Group'):
              self.set_Group(obj_.value)
        elif nodeName_ == 'ImagingStudy':
            obj_ = ImagingStudy.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'ImagingStudy', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_ImagingStudy'):
              self.add_ImagingStudy(obj_.value)
            elif hasattr(self, 'set_ImagingStudy'):
              self.set_ImagingStudy(obj_.value)
        elif nodeName_ == 'Immunization':
            obj_ = Immunization.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Immunization', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Immunization'):
              self.add_Immunization(obj_.value)
            elif hasattr(self, 'set_Immunization'):
              self.set_Immunization(obj_.value)
        elif nodeName_ == 'ImmunizationRecommendation':
            obj_ = ImmunizationRecommendation.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'ImmunizationRecommendation', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_ImmunizationRecommendation'):
              self.add_ImmunizationRecommendation(obj_.value)
            elif hasattr(self, 'set_ImmunizationRecommendation'):
              self.set_ImmunizationRecommendation(obj_.value)
        elif nodeName_ == 'List':
            obj_ = List.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'List', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_List'):
              self.add_List(obj_.value)
            elif hasattr(self, 'set_List'):
              self.set_List(obj_.value)
        elif nodeName_ == 'Location':
            obj_ = Location.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Location', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Location'):
              self.add_Location(obj_.value)
            elif hasattr(self, 'set_Location'):
              self.set_Location(obj_.value)
        elif nodeName_ == 'Media':
            obj_ = Media.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Media', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Media'):
              self.add_Media(obj_.value)
            elif hasattr(self, 'set_Media'):
              self.set_Media(obj_.value)
        elif nodeName_ == 'Medication':
            obj_ = Medication.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Medication', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Medication'):
              self.add_Medication(obj_.value)
            elif hasattr(self, 'set_Medication'):
              self.set_Medication(obj_.value)
        elif nodeName_ == 'MedicationAdministration':
            obj_ = MedicationAdministration.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'MedicationAdministration', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_MedicationAdministration'):
              self.add_MedicationAdministration(obj_.value)
            elif hasattr(self, 'set_MedicationAdministration'):
              self.set_MedicationAdministration(obj_.value)
        elif nodeName_ == 'MedicationDispense':
            obj_ = MedicationDispense.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'MedicationDispense', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_MedicationDispense'):
              self.add_MedicationDispense(obj_.value)
            elif hasattr(self, 'set_MedicationDispense'):
              self.set_MedicationDispense(obj_.value)
        elif nodeName_ == 'MedicationPrescription':
            obj_ = MedicationPrescription.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'MedicationPrescription', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_MedicationPrescription'):
              self.add_MedicationPrescription(obj_.value)
            elif hasattr(self, 'set_MedicationPrescription'):
              self.set_MedicationPrescription(obj_.value)
        elif nodeName_ == 'MedicationStatement':
            obj_ = MedicationStatement.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'MedicationStatement', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_MedicationStatement'):
              self.add_MedicationStatement(obj_.value)
            elif hasattr(self, 'set_MedicationStatement'):
              self.set_MedicationStatement(obj_.value)
        elif nodeName_ == 'MessageHeader':
            obj_ = MessageHeader.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'MessageHeader', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_MessageHeader'):
              self.add_MessageHeader(obj_.value)
            elif hasattr(self, 'set_MessageHeader'):
              self.set_MessageHeader(obj_.value)
        elif nodeName_ == 'Observation':
            obj_ = Observation.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Observation', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Observation'):
              self.add_Observation(obj_.value)
            elif hasattr(self, 'set_Observation'):
              self.set_Observation(obj_.value)
        elif nodeName_ == 'OperationOutcome':
            obj_ = OperationOutcome.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'OperationOutcome', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_OperationOutcome'):
              self.add_OperationOutcome(obj_.value)
            elif hasattr(self, 'set_OperationOutcome'):
              self.set_OperationOutcome(obj_.value)
        elif nodeName_ == 'Order':
            obj_ = Order.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Order', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Order'):
              self.add_Order(obj_.value)
            elif hasattr(self, 'set_Order'):
              self.set_Order(obj_.value)
        elif nodeName_ == 'OrderResponse':
            obj_ = OrderResponse.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'OrderResponse', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_OrderResponse'):
              self.add_OrderResponse(obj_.value)
            elif hasattr(self, 'set_OrderResponse'):
              self.set_OrderResponse(obj_.value)
        elif nodeName_ == 'Organization':
            obj_ = Organization.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Organization', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Organization'):
              self.add_Organization(obj_.value)
            elif hasattr(self, 'set_Organization'):
              self.set_Organization(obj_.value)
        elif nodeName_ == 'Other':
            obj_ = Other.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Other', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Other'):
              self.add_Other(obj_.value)
            elif hasattr(self, 'set_Other'):
              self.set_Other(obj_.value)
        elif nodeName_ == 'Patient':
            obj_ = Patient.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Patient', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Patient'):
              self.add_Patient(obj_.value)
            elif hasattr(self, 'set_Patient'):
              self.set_Patient(obj_.value)
        elif nodeName_ == 'Practitioner':
            obj_ = Practitioner.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Practitioner', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Practitioner'):
              self.add_Practitioner(obj_.value)
            elif hasattr(self, 'set_Practitioner'):
              self.set_Practitioner(obj_.value)
        elif nodeName_ == 'Procedure':
            obj_ = Procedure.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Procedure', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Procedure'):
              self.add_Procedure(obj_.value)
            elif hasattr(self, 'set_Procedure'):
              self.set_Procedure(obj_.value)
        elif nodeName_ == 'Profile':
            obj_ = Profile.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Profile', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Profile'):
              self.add_Profile(obj_.value)
            elif hasattr(self, 'set_Profile'):
              self.set_Profile(obj_.value)
        elif nodeName_ == 'Provenance':
            obj_ = Provenance.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Provenance', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Provenance'):
              self.add_Provenance(obj_.value)
            elif hasattr(self, 'set_Provenance'):
              self.set_Provenance(obj_.value)
        elif nodeName_ == 'Query':
            obj_ = Query.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Query', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Query'):
              self.add_Query(obj_.value)
            elif hasattr(self, 'set_Query'):
              self.set_Query(obj_.value)
        elif nodeName_ == 'Questionnaire':
            obj_ = Questionnaire.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Questionnaire', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Questionnaire'):
              self.add_Questionnaire(obj_.value)
            elif hasattr(self, 'set_Questionnaire'):
              self.set_Questionnaire(obj_.value)
        elif nodeName_ == 'RelatedPerson':
            obj_ = RelatedPerson.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'RelatedPerson', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_RelatedPerson'):
              self.add_RelatedPerson(obj_.value)
            elif hasattr(self, 'set_RelatedPerson'):
              self.set_RelatedPerson(obj_.value)
        elif nodeName_ == 'SecurityEvent':
            obj_ = SecurityEvent.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'SecurityEvent', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_SecurityEvent'):
              self.add_SecurityEvent(obj_.value)
            elif hasattr(self, 'set_SecurityEvent'):
              self.set_SecurityEvent(obj_.value)
        elif nodeName_ == 'Specimen':
            obj_ = Specimen.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Specimen', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Specimen'):
              self.add_Specimen(obj_.value)
            elif hasattr(self, 'set_Specimen'):
              self.set_Specimen(obj_.value)
        elif nodeName_ == 'Substance':
            obj_ = Substance.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Substance', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Substance'):
              self.add_Substance(obj_.value)
            elif hasattr(self, 'set_Substance'):
              self.set_Substance(obj_.value)
        elif nodeName_ == 'Supply':
            obj_ = Supply.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'Supply', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_Supply'):
              self.add_Supply(obj_.value)
            elif hasattr(self, 'set_Supply'):
              self.set_Supply(obj_.value)
        elif nodeName_ == 'ValueSet':
            obj_ = ValueSet.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'ValueSet', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_ValueSet'):
              self.add_ValueSet(obj_.value)
            elif hasattr(self, 'set_ValueSet'):
              self.set_ValueSet(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)

class UriType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, base=None, valueOf_=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.base = _cast(None, base)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if UriType.subclass:
            return UriType.subclass(*args_, **kwargs_)
        else:
            return UriType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_base(self): return self.base
    def set_base(self, base): self.base = base
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='UriType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, (' ' + namespacedef_ or '').rstrip(), ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='UriType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_='', name_='UriType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='UriType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            outfile.write(' base=%s' % (self.gds_format_string(quote_attrib(self.base).encode(ExternalEncoding), input_name='base'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='UriType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='UriType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            showIndent(outfile, level)
            outfile.write('lang="%s",\n' % (self.lang,))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            showIndent(outfile, level)
            outfile.write('base="%s",\n' % (self.base,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
        value = find_attr_value_('base', node)
        if value is not None and 'base' not in already_processed:
            already_processed.add('base')
            self.base = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass

class IdType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, base=None, valueOf_=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.base = _cast(None, base)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if IdType.subclass:
            return IdType.subclass(*args_, **kwargs_)
        else:
            return IdType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_base(self): return self.base
    def set_base(self, base): self.base = base
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='IdType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IdType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_='', name_='IdType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='IdType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            outfile.write(' base=%s' % (self.gds_format_string(quote_attrib(self.base).encode(ExternalEncoding), input_name='base'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='IdType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='IdType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            showIndent(outfile, level)
            outfile.write('lang="%s",\n' % (self.lang,))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            showIndent(outfile, level)
            outfile.write('base="%s",\n' % (self.base,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
        value = find_attr_value_('base', node)
        if value is not None and 'base' not in already_processed:
            already_processed.add('base')
            self.base = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass

class TextType(GeneratedsSuper):
    """The Atom text construct is defined in section 3.1 of the format
    spec."""
    subclass = None
    superclass = None
    def __init__(self, lang=None, base=None, type_=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.base = _cast(None, base)
        self.type_ = _cast(None, type_)
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if TextType.subclass:
            return TextType.subclass(*args_, **kwargs_)
        else:
            return TextType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_base(self): return self.base
    def set_base(self, base): self.base = base
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.anytypeobjs_ is not None or
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='TextType', namespacedef_='', pretty_print=False):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, (' ' + namespacedef_ or '').rstrip(), ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='TextType')
        if self.hasContent_():
            outfile.write('>%s' % ('', ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='TextType', pretty_print=False)
            #showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='TextType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            outfile.write(' base=%s' % (self.gds_format_string(quote_attrib(self.base).encode(ExternalEncoding), input_name='base'), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_format_string(quote_attrib(self.type_).encode(ExternalEncoding), input_name='type'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='TextType', fromsubclass_=False, pretty_print=False):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='TextType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            showIndent(outfile, level)
            outfile.write('lang="%s",\n' % (self.lang,))
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            showIndent(outfile, level)
            outfile.write('base="%s",\n' % (self.base,))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            showIndent(outfile, level)
            outfile.write('type_="%s",\n' % (self.type_,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
        value = find_attr_value_('base', node)
        if value is not None and 'base' not in already_processed:
            already_processed.add('base')
            self.base = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.type_ = ' '.join(self.type_.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == '':
            obj_ = __ANY__.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)

class linkType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, href=None, rel=None):
        self.original_tagname_ = None
        self.href = _cast(None, href)
        self.rel = _cast(None, rel)
    def factory(*args_, **kwargs_):
        if linkType.subclass:
            return linkType.subclass(*args_, **kwargs_)
        else:
            return linkType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_href(self): return self.href
    def set_href(self, href): self.href = href
    def get_rel(self): return self.rel
    def set_rel(self, rel): self.rel = rel
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='linkType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, (' ' + namespacedef_ or '').rstrip(), ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='linkType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='linkType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='linkType'):
        if self.href is not None and 'href' not in already_processed:
            already_processed.add('href')
            outfile.write(' href=%s' % (self.gds_format_string(quote_attrib(self.href).encode(ExternalEncoding), input_name='href'), ))
        if self.rel is not None and 'rel' not in already_processed:
            already_processed.add('rel')
            outfile.write(' rel=%s' % (self.gds_format_string(quote_attrib(self.rel).encode(ExternalEncoding), input_name='rel'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='linkType', fromsubclass_=False, pretty_print=True):
        pass
    def exportLiteral(self, outfile, level, name_='linkType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.href is not None and 'href' not in already_processed:
            already_processed.add('href')
            showIndent(outfile, level)
            outfile.write('href="%s",\n' % (self.href,))
        if self.rel is not None and 'rel' not in already_processed:
            already_processed.add('rel')
            showIndent(outfile, level)
            outfile.write('rel="%s",\n' % (self.rel,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('href', node)
        if value is not None and 'href' not in already_processed:
            already_processed.add('href')
            self.href = value
        value = find_attr_value_('rel', node)
        if value is not None and 'rel' not in already_processed:
            already_processed.add('rel')
            self.rel = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
