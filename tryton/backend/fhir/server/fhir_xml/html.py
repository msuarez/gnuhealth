from .base_classes import *
from .support_functions import *


class a_content(GeneratedsSuper):
    """a elements use "Inline" excluding a"""
    subclass = None
    superclass = None
    def __init__(self, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None):
        self.original_tagname_ = None
        self.br = br
        self.span = span
        self.bdo = bdo
        self.map = map
        self.img = img
        self.tt = tt
        self.i = i
        self.b = b
        self.big = big
        self.small = small
        self.em = em
        self.strong = strong
        self.dfn = dfn
        self.code = code
        self.q = q
        self.samp = samp
        self.kbd = kbd
        self.var = var
        self.cite = cite
        self.abbr = abbr
        self.acronym = acronym
        self.sub = sub
        self.sup = sup
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_
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
        if a_content.subclass:
            return a_content.subclass(*args_, **kwargs_)
        else:
            return a_content(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_br(self): return self.br
    def set_br(self, br): self.br = br
    def get_span(self): return self.span
    def set_span(self, span): self.span = span
    def get_bdo(self): return self.bdo
    def set_bdo(self, bdo): self.bdo = bdo
    def get_map(self): return self.map
    def set_map(self, map): self.map = map
    def get_img(self): return self.img
    def set_img(self, img): self.img = img
    def get_tt(self): return self.tt
    def set_tt(self, tt): self.tt = tt
    def get_i(self): return self.i
    def set_i(self, i): self.i = i
    def get_b(self): return self.b
    def set_b(self, b): self.b = b
    def get_big(self): return self.big
    def set_big(self, big): self.big = big
    def get_small(self): return self.small
    def set_small(self, small): self.small = small
    def get_em(self): return self.em
    def set_em(self, em): self.em = em
    def get_strong(self): return self.strong
    def set_strong(self, strong): self.strong = strong
    def get_dfn(self): return self.dfn
    def set_dfn(self, dfn): self.dfn = dfn
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_q(self): return self.q
    def set_q(self, q): self.q = q
    def get_samp(self): return self.samp
    def set_samp(self, samp): self.samp = samp
    def get_kbd(self): return self.kbd
    def set_kbd(self, kbd): self.kbd = kbd
    def get_var(self): return self.var
    def set_var(self, var): self.var = var
    def get_cite(self): return self.cite
    def set_cite(self, cite): self.cite = cite
    def get_abbr(self): return self.abbr
    def set_abbr(self, abbr): self.abbr = abbr
    def get_acronym(self): return self.acronym
    def set_acronym(self, acronym): self.acronym = acronym
    def get_sub(self): return self.sub
    def set_sub(self, sub): self.sub = sub
    def get_sup(self): return self.sup
    def set_sup(self, sup): self.sup = sup
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.br is not None or
            self.span is not None or
            self.bdo is not None or
            self.map is not None or
            self.img is not None or
            self.tt is not None or
            self.i is not None or
            self.b is not None or
            self.big is not None or
            self.small is not None or
            self.em is not None or
            self.strong is not None or
            self.dfn is not None or
            self.code is not None or
            self.q is not None or
            self.samp is not None or
            self.kbd is not None or
            self.var is not None or
            self.cite is not None or
            self.abbr is not None or
            self.acronym is not None or
            self.sub is not None or
            self.sup is not None or
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='a.content', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='a.content')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='a.content', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='a.content'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='a.content', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='a.content', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        for item_ in self.content_:
            item_.to_etree(element)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'br':
            obj_ = br.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'br', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_br'):
              self.add_br(obj_.value)
            elif hasattr(self, 'set_br'):
              self.set_br(obj_.value)
        elif nodeName_ == 'span':
            obj_ = span.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'span', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_span'):
              self.add_span(obj_.value)
            elif hasattr(self, 'set_span'):
              self.set_span(obj_.value)
        elif nodeName_ == 'bdo':
            obj_ = bdo.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'bdo', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_bdo'):
              self.add_bdo(obj_.value)
            elif hasattr(self, 'set_bdo'):
              self.set_bdo(obj_.value)
        elif nodeName_ == 'map':
            obj_ = map.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'map', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_map'):
              self.add_map(obj_.value)
            elif hasattr(self, 'set_map'):
              self.set_map(obj_.value)
        elif nodeName_ == 'img':
            obj_ = img.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'img', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_img'):
              self.add_img(obj_.value)
            elif hasattr(self, 'set_img'):
              self.set_img(obj_.value)
        elif nodeName_ == 'tt':
            obj_ = tt.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'tt', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_tt'):
              self.add_tt(obj_.value)
            elif hasattr(self, 'set_tt'):
              self.set_tt(obj_.value)
        elif nodeName_ == 'i':
            obj_ = i.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'i', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_i'):
              self.add_i(obj_.value)
            elif hasattr(self, 'set_i'):
              self.set_i(obj_.value)
        elif nodeName_ == 'b':
            obj_ = b.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'b', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_b'):
              self.add_b(obj_.value)
            elif hasattr(self, 'set_b'):
              self.set_b(obj_.value)
        elif nodeName_ == 'big':
            obj_ = big.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'big', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_big'):
              self.add_big(obj_.value)
            elif hasattr(self, 'set_big'):
              self.set_big(obj_.value)
        elif nodeName_ == 'small':
            obj_ = small.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'small', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_small'):
              self.add_small(obj_.value)
            elif hasattr(self, 'set_small'):
              self.set_small(obj_.value)
        elif nodeName_ == 'em':
            obj_ = em.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'em', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_em'):
              self.add_em(obj_.value)
            elif hasattr(self, 'set_em'):
              self.set_em(obj_.value)
        elif nodeName_ == 'strong':
            obj_ = strong.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'strong', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_strong'):
              self.add_strong(obj_.value)
            elif hasattr(self, 'set_strong'):
              self.set_strong(obj_.value)
        elif nodeName_ == 'dfn':
            obj_ = dfn.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'dfn', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_dfn'):
              self.add_dfn(obj_.value)
            elif hasattr(self, 'set_dfn'):
              self.set_dfn(obj_.value)
        elif nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'code', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_code'):
              self.add_code(obj_.value)
            elif hasattr(self, 'set_code'):
              self.set_code(obj_.value)
        elif nodeName_ == 'q':
            obj_ = q.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'q', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_q'):
              self.add_q(obj_.value)
            elif hasattr(self, 'set_q'):
              self.set_q(obj_.value)
        elif nodeName_ == 'samp':
            obj_ = samp.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'samp', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_samp'):
              self.add_samp(obj_.value)
            elif hasattr(self, 'set_samp'):
              self.set_samp(obj_.value)
        elif nodeName_ == 'kbd':
            obj_ = kbd.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'kbd', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_kbd'):
              self.add_kbd(obj_.value)
            elif hasattr(self, 'set_kbd'):
              self.set_kbd(obj_.value)
        elif nodeName_ == 'var':
            obj_ = var.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'var', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_var'):
              self.add_var(obj_.value)
            elif hasattr(self, 'set_var'):
              self.set_var(obj_.value)
        elif nodeName_ == 'cite':
            obj_ = cite.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'cite', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_cite'):
              self.add_cite(obj_.value)
            elif hasattr(self, 'set_cite'):
              self.set_cite(obj_.value)
        elif nodeName_ == 'abbr':
            obj_ = abbr.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'abbr', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_abbr'):
              self.add_abbr(obj_.value)
            elif hasattr(self, 'set_abbr'):
              self.set_abbr(obj_.value)
        elif nodeName_ == 'acronym':
            obj_ = acronym.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'acronym', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_acronym'):
              self.add_acronym(obj_.value)
            elif hasattr(self, 'set_acronym'):
              self.set_acronym(obj_.value)
        elif nodeName_ == 'sub':
            obj_ = sub.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'sub', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_sub'):
              self.add_sub(obj_.value)
            elif hasattr(self, 'set_sub'):
              self.set_sub(obj_.value)
        elif nodeName_ == 'sup':
            obj_ = sup.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'sup', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_sup'):
              self.add_sup(obj_.value)
            elif hasattr(self, 'set_sup'):
              self.set_sup(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class a_content


class pre_content(GeneratedsSuper):
    """pre uses "Inline" excluding big, small, sup or sup"""
    subclass = None
    superclass = None
    def __init__(self, a=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, br=None, span=None, bdo=None, map=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None):
        self.original_tagname_ = None
        if a is None:
            self.a = []
        else:
            self.a = a
        self.tt = tt
        self.i = i
        self.b = b
        self.big = big
        self.small = small
        self.em = em
        self.strong = strong
        self.dfn = dfn
        self.code = code
        self.q = q
        self.samp = samp
        self.kbd = kbd
        self.var = var
        self.cite = cite
        self.abbr = abbr
        self.acronym = acronym
        self.sub = sub
        self.sup = sup
        self.br = br
        self.span = span
        self.bdo = bdo
        self.map = map
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_
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
        if pre_content.subclass:
            return pre_content.subclass(*args_, **kwargs_)
        else:
            return pre_content(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_a(self): return self.a
    def set_a(self, a): self.a = a
    def add_a(self, value): self.a.append(value)
    def insert_a(self, index, value): self.a[index] = value
    def get_tt(self): return self.tt
    def set_tt(self, tt): self.tt = tt
    def get_i(self): return self.i
    def set_i(self, i): self.i = i
    def get_b(self): return self.b
    def set_b(self, b): self.b = b
    def get_big(self): return self.big
    def set_big(self, big): self.big = big
    def get_small(self): return self.small
    def set_small(self, small): self.small = small
    def get_em(self): return self.em
    def set_em(self, em): self.em = em
    def get_strong(self): return self.strong
    def set_strong(self, strong): self.strong = strong
    def get_dfn(self): return self.dfn
    def set_dfn(self, dfn): self.dfn = dfn
    def get_code(self): return self.code
    def set_code(self, code): self.code = code
    def get_q(self): return self.q
    def set_q(self, q): self.q = q
    def get_samp(self): return self.samp
    def set_samp(self, samp): self.samp = samp
    def get_kbd(self): return self.kbd
    def set_kbd(self, kbd): self.kbd = kbd
    def get_var(self): return self.var
    def set_var(self, var): self.var = var
    def get_cite(self): return self.cite
    def set_cite(self, cite): self.cite = cite
    def get_abbr(self): return self.abbr
    def set_abbr(self, abbr): self.abbr = abbr
    def get_acronym(self): return self.acronym
    def set_acronym(self, acronym): self.acronym = acronym
    def get_sub(self): return self.sub
    def set_sub(self, sub): self.sub = sub
    def get_sup(self): return self.sup
    def set_sup(self, sup): self.sup = sup
    def get_br(self): return self.br
    def set_br(self, br): self.br = br
    def get_span(self): return self.span
    def set_span(self, span): self.span = span
    def get_bdo(self): return self.bdo
    def set_bdo(self, bdo): self.bdo = bdo
    def get_map(self): return self.map
    def set_map(self, map): self.map = map
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.a or
            self.tt is not None or
            self.i is not None or
            self.b is not None or
            self.big is not None or
            self.small is not None or
            self.em is not None or
            self.strong is not None or
            self.dfn is not None or
            self.code is not None or
            self.q is not None or
            self.samp is not None or
            self.kbd is not None or
            self.var is not None or
            self.cite is not None or
            self.abbr is not None or
            self.acronym is not None or
            self.sub is not None or
            self.sup is not None or
            self.br is not None or
            self.span is not None or
            self.bdo is not None or
            self.map is not None or
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='pre.content', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='pre.content')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='pre.content', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='pre.content'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='pre.content', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='pre.content', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        for item_ in self.content_:
            item_.to_etree(element)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'a':
            obj_ = a.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'a', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_a'):
              self.add_a(obj_.value)
            elif hasattr(self, 'set_a'):
              self.set_a(obj_.value)
        elif nodeName_ == 'tt':
            obj_ = tt.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'tt', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_tt'):
              self.add_tt(obj_.value)
            elif hasattr(self, 'set_tt'):
              self.set_tt(obj_.value)
        elif nodeName_ == 'i':
            obj_ = i.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'i', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_i'):
              self.add_i(obj_.value)
            elif hasattr(self, 'set_i'):
              self.set_i(obj_.value)
        elif nodeName_ == 'b':
            obj_ = b.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'b', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_b'):
              self.add_b(obj_.value)
            elif hasattr(self, 'set_b'):
              self.set_b(obj_.value)
        elif nodeName_ == 'big':
            obj_ = big.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'big', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_big'):
              self.add_big(obj_.value)
            elif hasattr(self, 'set_big'):
              self.set_big(obj_.value)
        elif nodeName_ == 'small':
            obj_ = small.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'small', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_small'):
              self.add_small(obj_.value)
            elif hasattr(self, 'set_small'):
              self.set_small(obj_.value)
        elif nodeName_ == 'em':
            obj_ = em.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'em', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_em'):
              self.add_em(obj_.value)
            elif hasattr(self, 'set_em'):
              self.set_em(obj_.value)
        elif nodeName_ == 'strong':
            obj_ = strong.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'strong', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_strong'):
              self.add_strong(obj_.value)
            elif hasattr(self, 'set_strong'):
              self.set_strong(obj_.value)
        elif nodeName_ == 'dfn':
            obj_ = dfn.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'dfn', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_dfn'):
              self.add_dfn(obj_.value)
            elif hasattr(self, 'set_dfn'):
              self.set_dfn(obj_.value)
        elif nodeName_ == 'code':
            obj_ = code.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'code', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_code'):
              self.add_code(obj_.value)
            elif hasattr(self, 'set_code'):
              self.set_code(obj_.value)
        elif nodeName_ == 'q':
            obj_ = q.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'q', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_q'):
              self.add_q(obj_.value)
            elif hasattr(self, 'set_q'):
              self.set_q(obj_.value)
        elif nodeName_ == 'samp':
            obj_ = samp.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'samp', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_samp'):
              self.add_samp(obj_.value)
            elif hasattr(self, 'set_samp'):
              self.set_samp(obj_.value)
        elif nodeName_ == 'kbd':
            obj_ = kbd.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'kbd', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_kbd'):
              self.add_kbd(obj_.value)
            elif hasattr(self, 'set_kbd'):
              self.set_kbd(obj_.value)
        elif nodeName_ == 'var':
            obj_ = var.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'var', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_var'):
              self.add_var(obj_.value)
            elif hasattr(self, 'set_var'):
              self.set_var(obj_.value)
        elif nodeName_ == 'cite':
            obj_ = cite.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'cite', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_cite'):
              self.add_cite(obj_.value)
            elif hasattr(self, 'set_cite'):
              self.set_cite(obj_.value)
        elif nodeName_ == 'abbr':
            obj_ = abbr.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'abbr', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_abbr'):
              self.add_abbr(obj_.value)
            elif hasattr(self, 'set_abbr'):
              self.set_abbr(obj_.value)
        elif nodeName_ == 'acronym':
            obj_ = acronym.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'acronym', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_acronym'):
              self.add_acronym(obj_.value)
            elif hasattr(self, 'set_acronym'):
              self.set_acronym(obj_.value)
        elif nodeName_ == 'sub':
            obj_ = sub.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'sub', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_sub'):
              self.add_sub(obj_.value)
            elif hasattr(self, 'set_sub'):
              self.set_sub(obj_.value)
        elif nodeName_ == 'sup':
            obj_ = sup.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'sup', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_sup'):
              self.add_sup(obj_.value)
            elif hasattr(self, 'set_sup'):
              self.set_sup(obj_.value)
        elif nodeName_ == 'br':
            obj_ = br.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'br', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_br'):
              self.add_br(obj_.value)
            elif hasattr(self, 'set_br'):
              self.set_br(obj_.value)
        elif nodeName_ == 'span':
            obj_ = span.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'span', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_span'):
              self.add_span(obj_.value)
            elif hasattr(self, 'set_span'):
              self.set_span(obj_.value)
        elif nodeName_ == 'bdo':
            obj_ = bdo.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'bdo', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_bdo'):
              self.add_bdo(obj_.value)
            elif hasattr(self, 'set_bdo'):
              self.set_bdo(obj_.value)
        elif nodeName_ == 'map':
            obj_ = map.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'map', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_map'):
              self.add_map(obj_.value)
            elif hasattr(self, 'set_map'):
              self.set_map(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class pre_content


class div(Flow):
    """generic language/style container"""
    subclass = None
    superclass = Flow
    def __init__(self, p=None, h1=None, h2=None, h3=None, h4=None, h5=None, h6=None, div_=None, ul=None, ol=None, dl=None, pre=None, hr=None, blockquote=None, table=None, a=None, br=None, span=None, bdo=None, map_=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(div, self).__init__(p, h1, h2, h3, h4, h5, h6, div_, ul, ol, dl, pre, hr, blockquote, table, a, br, span, bdo, map_, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if div.subclass:
            return div.subclass(*args_, **kwargs_)
        else:
            return div(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(div, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='div', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='div')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='div', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='div'):
        super(div, self).exportAttributes(outfile, level, already_processed, namespace_, name_='div')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='div', fromsubclass_=False, pretty_print=True):
        super(div, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='div', mapping_=None):
        element = super(div, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(div, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(div, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class div


class p(Inline):
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(p, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if p.subclass:
            return p.subclass(*args_, **kwargs_)
        else:
            return p(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(p, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='p', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='p')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='p', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='p'):
        super(p, self).exportAttributes(outfile, level, already_processed, namespace_, name_='p')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='p', fromsubclass_=False, pretty_print=True):
        super(p, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='p', mapping_=None):
        element = super(p, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(p, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(p, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class p


class h1(Inline):
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(h1, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if h1.subclass:
            return h1.subclass(*args_, **kwargs_)
        else:
            return h1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(h1, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='h1', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='h1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='h1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='h1'):
        super(h1, self).exportAttributes(outfile, level, already_processed, namespace_, name_='h1')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='h1', fromsubclass_=False, pretty_print=True):
        super(h1, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='h1', mapping_=None):
        element = super(h1, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(h1, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(h1, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class h1


class h2(Inline):
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(h2, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if h2.subclass:
            return h2.subclass(*args_, **kwargs_)
        else:
            return h2(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(h2, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='h2', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='h2')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='h2', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='h2'):
        super(h2, self).exportAttributes(outfile, level, already_processed, namespace_, name_='h2')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='h2', fromsubclass_=False, pretty_print=True):
        super(h2, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='h2', mapping_=None):
        element = super(h2, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(h2, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(h2, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class h2


class h3(Inline):
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(h3, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if h3.subclass:
            return h3.subclass(*args_, **kwargs_)
        else:
            return h3(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(h3, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='h3', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='h3')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='h3', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='h3'):
        super(h3, self).exportAttributes(outfile, level, already_processed, namespace_, name_='h3')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='h3', fromsubclass_=False, pretty_print=True):
        super(h3, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='h3', mapping_=None):
        element = super(h3, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(h3, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(h3, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class h3


class h4(Inline):
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(h4, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if h4.subclass:
            return h4.subclass(*args_, **kwargs_)
        else:
            return h4(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(h4, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='h4', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='h4')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='h4', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='h4'):
        super(h4, self).exportAttributes(outfile, level, already_processed, namespace_, name_='h4')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='h4', fromsubclass_=False, pretty_print=True):
        super(h4, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='h4', mapping_=None):
        element = super(h4, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(h4, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(h4, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class h4


class h5(Inline):
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(h5, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if h5.subclass:
            return h5.subclass(*args_, **kwargs_)
        else:
            return h5(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(h5, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='h5', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='h5')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='h5', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='h5'):
        super(h5, self).exportAttributes(outfile, level, already_processed, namespace_, name_='h5')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='h5', fromsubclass_=False, pretty_print=True):
        super(h5, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='h5', mapping_=None):
        element = super(h5, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(h5, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(h5, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class h5


class h6(Inline):
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(h6, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if h6.subclass:
            return h6.subclass(*args_, **kwargs_)
        else:
            return h6(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(h6, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='h6', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='h6')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='h6', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='h6'):
        super(h6, self).exportAttributes(outfile, level, already_processed, namespace_, name_='h6')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='h6', fromsubclass_=False, pretty_print=True):
        super(h6, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='h6', mapping_=None):
        element = super(h6, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(h6, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(h6, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class h6


class ul(GeneratedsSuper):
    """Unordered list"""
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, title=None, id=None, class_=None, dir=None, li=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
        if li is None:
            self.li = []
        else:
            self.li = li
    def factory(*args_, **kwargs_):
        if ul.subclass:
            return ul.subclass(*args_, **kwargs_)
        else:
            return ul(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_li(self): return self.li
    def set_li(self, li): self.li = li
    def add_li(self, value): self.li.append(value)
    def insert_li(self, index, value): self.li[index] = value
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.li
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ul', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ul')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ul', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ul'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ul', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for li_ in self.li:
            li_.export(outfile, level, namespace_, name_='li', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ul', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        for li_ in self.li:
            li_.to_etree(element, name_='li', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'li':
            obj_ = li.factory()
            obj_.build(child_)
            self.li.append(obj_)
            obj_.original_tagname_ = 'li'
# end class ul


class ol(GeneratedsSuper):
    """Ordered (numbered) list"""
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, title=None, id=None, class_=None, dir=None, li=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
        if li is None:
            self.li = []
        else:
            self.li = li
    def factory(*args_, **kwargs_):
        if ol.subclass:
            return ol.subclass(*args_, **kwargs_)
        else:
            return ol(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_li(self): return self.li
    def set_li(self, li): self.li = li
    def add_li(self, value): self.li.append(value)
    def insert_li(self, index, value): self.li[index] = value
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.li
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ol', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ol')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ol', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ol'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ol', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for li_ in self.li:
            li_.export(outfile, level, namespace_, name_='li', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ol', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        for li_ in self.li:
            li_.to_etree(element, name_='li', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'li':
            obj_ = li.factory()
            obj_.build(child_)
            self.li.append(obj_)
            obj_.original_tagname_ = 'li'
# end class ol


class li(Flow):
    """list item"""
    subclass = None
    superclass = Flow
    def __init__(self, p=None, h1=None, h2=None, h3=None, h4=None, h5=None, h6=None, div=None, ul=None, ol=None, dl=None, pre=None, hr=None, blockquote=None, table=None, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(li, self).__init__(p, h1, h2, h3, h4, h5, h6, div, ul, ol, dl, pre, hr, blockquote, table, a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if li.subclass:
            return li.subclass(*args_, **kwargs_)
        else:
            return li(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(li, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='li', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='li')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='li', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='li'):
        super(li, self).exportAttributes(outfile, level, already_processed, namespace_, name_='li')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='li', fromsubclass_=False, pretty_print=True):
        super(li, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='li', mapping_=None):
        element = super(li, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(li, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(li, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class li


class dl(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, title=None, id=None, class_=None, dir=None, dt=None, dd=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
        if dt is None:
            self.dt = []
        else:
            self.dt = dt
        if dd is None:
            self.dd = []
        else:
            self.dd = dd
    def factory(*args_, **kwargs_):
        if dl.subclass:
            return dl.subclass(*args_, **kwargs_)
        else:
            return dl(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_dt(self): return self.dt
    def set_dt(self, dt): self.dt = dt
    def add_dt(self, value): self.dt.append(value)
    def insert_dt(self, index, value): self.dt[index] = value
    def get_dd(self): return self.dd
    def set_dd(self, dd): self.dd = dd
    def add_dd(self, value): self.dd.append(value)
    def insert_dd(self, index, value): self.dd[index] = value
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.dt or
            self.dd
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='dl', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='dl')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='dl', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='dl'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='dl', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for dt_ in self.dt:
            dt_.export(outfile, level, namespace_, name_='dt', pretty_print=pretty_print)
        for dd_ in self.dd:
            dd_.export(outfile, level, namespace_, name_='dd', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='dl', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        for dt_ in self.dt:
            dt_.to_etree(element, name_='dt', mapping_=mapping_)
        for dd_ in self.dd:
            dd_.to_etree(element, name_='dd', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'dt':
            obj_ = dt.factory()
            obj_.build(child_)
            self.dt.append(obj_)
            obj_.original_tagname_ = 'dt'
        elif nodeName_ == 'dd':
            obj_ = dd.factory()
            obj_.build(child_)
            self.dd.append(obj_)
            obj_.original_tagname_ = 'dd'
# end class dl


class dt(Inline):
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(dt, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if dt.subclass:
            return dt.subclass(*args_, **kwargs_)
        else:
            return dt(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(dt, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='dt', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='dt')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='dt', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='dt'):
        super(dt, self).exportAttributes(outfile, level, already_processed, namespace_, name_='dt')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='dt', fromsubclass_=False, pretty_print=True):
        super(dt, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='dt', mapping_=None):
        element = super(dt, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(dt, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(dt, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class dt


class dd(Flow):
    subclass = None
    superclass = Flow
    def __init__(self, p=None, h1=None, h2=None, h3=None, h4=None, h5=None, h6=None, div=None, ul=None, ol=None, dl=None, pre=None, hr=None, blockquote=None, table=None, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(dd, self).__init__(p, h1, h2, h3, h4, h5, h6, div, ul, ol, dl, pre, hr, blockquote, table, a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if dd.subclass:
            return dd.subclass(*args_, **kwargs_)
        else:
            return dd(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(dd, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='dd', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='dd')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='dd', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='dd'):
        super(dd, self).exportAttributes(outfile, level, already_processed, namespace_, name_='dd')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='dd', fromsubclass_=False, pretty_print=True):
        super(dd, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='dd', mapping_=None):
        element = super(dd, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(dd, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(dd, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class dd


class hr(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, title=None, id=None, class_=None, dir=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
    def factory(*args_, **kwargs_):
        if hr.subclass:
            return hr.subclass(*args_, **kwargs_)
        else:
            return hr(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='hr', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='hr')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='hr', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='hr'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='hr', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='hr', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class hr


class pre(pre_content):
    """ content is "Inline" excluding "img|object|big|small|sub|sup" """
    subclass = None
    superclass = pre_content
    def __init__(self, a=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, br=None, span=None, bdo=None, map=None, lang=None, style=None, title=None, space=None, class_=None, id=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(pre, self).__init__(a, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, br, span, bdo, map, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.space = _cast(None, space)
        self.class_ = _cast(None, class_)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
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
        if pre.subclass:
            return pre.subclass(*args_, **kwargs_)
        else:
            return pre(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_space(self): return self.space
    def set_space(self, space): self.space = space
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(pre, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='pre', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='pre')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='pre', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='pre'):
        super(pre, self).exportAttributes(outfile, level, already_processed, namespace_, name_='pre')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.space is not None and 'space' not in already_processed:
            already_processed.add('space')
            outfile.write(' space=%s' % (self.gds_format_string(quote_attrib(self.space).encode(ExternalEncoding), input_name='space'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='pre', fromsubclass_=False, pretty_print=True):
        super(pre, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='pre', mapping_=None):
        element = super(pre, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.space is not None:
            element.set('space', self.gds_format_string(self.space))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('space', node)
        if value is not None and 'space' not in already_processed:
            already_processed.add('space')
            self.space = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(pre, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(pre, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class pre


class blockquote(Block):
    subclass = None
    superclass = Block
    def __init__(self, p=None, h1=None, h2=None, h3=None, h4=None, h5=None, h6=None, div=None, ul=None, ol=None, dl=None, pre=None, hr=None, blockquote_=None, table=None, lang=None, style=None, title=None, class_=None, cite=None, id=None, dir=None):
        self.original_tagname_ = None
        super(blockquote, self).__init__(p, h1, h2, h3, h4, h5, h6, div, ul, ol, dl, pre, hr, blockquote_, table, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.class_ = _cast(None, class_)
        self.cite = _cast(None, cite)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
    def factory(*args_, **kwargs_):
        if blockquote.subclass:
            return blockquote.subclass(*args_, **kwargs_)
        else:
            return blockquote(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_cite(self): return self.cite
    def set_cite(self, cite): self.cite = cite
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_URI(self, value):
        # Validate type URI, a restriction on xs:anyURI.
        pass
    def hasContent_(self):
        if (
            super(blockquote, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='blockquote', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='blockquote')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='blockquote', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='blockquote'):
        super(blockquote, self).exportAttributes(outfile, level, already_processed, namespace_, name_='blockquote')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.cite is not None and 'cite' not in already_processed:
            already_processed.add('cite')
            outfile.write(' cite=%s' % (quote_attrib(self.cite), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='blockquote', fromsubclass_=False, pretty_print=True):
        super(blockquote, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='blockquote', mapping_=None):
        element = super(blockquote, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.cite is not None:
            element.set('cite', self.cite)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('cite', node)
        if value is not None and 'cite' not in already_processed:
            already_processed.add('cite')
            self.cite = value
            self.validate_URI(self.cite)    # validate type URI
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(blockquote, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(blockquote, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class blockquote


class a(a_content):
    """content is "Inline" except that anchors shouldn't be nested"""
    subclass = None
    superclass = a_content
    def __init__(self, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, name=None, title=None, class_=None, charset=None, rev=None, hreflang=None, shape='rect', href=None, coords=None, accesskey=None, rel=None, type_=None, id=None, dir=None, tabindex=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(a, self).__init__(br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.name = _cast(None, name)
        self.title = _cast(None, title)
        self.class_ = _cast(None, class_)
        self.charset = _cast(None, charset)
        self.rev = _cast(None, rev)
        self.hreflang = _cast(None, hreflang)
        self.shape = _cast(None, shape)
        self.href = _cast(None, href)
        self.coords = _cast(None, coords)
        self.accesskey = _cast(None, accesskey)
        self.rel = _cast(None, rel)
        self.type_ = _cast(None, type_)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
        self.tabindex = _cast(None, tabindex)
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
        if a.subclass:
            return a.subclass(*args_, **kwargs_)
        else:
            return a(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_charset(self): return self.charset
    def set_charset(self, charset): self.charset = charset
    def get_rev(self): return self.rev
    def set_rev(self, rev): self.rev = rev
    def get_hreflang(self): return self.hreflang
    def set_hreflang(self, hreflang): self.hreflang = hreflang
    def get_shape(self): return self.shape
    def set_shape(self, shape): self.shape = shape
    def get_href(self): return self.href
    def set_href(self, href): self.href = href
    def get_coords(self): return self.coords
    def set_coords(self, coords): self.coords = coords
    def get_accesskey(self): return self.accesskey
    def set_accesskey(self, accesskey): self.accesskey = accesskey
    def get_rel(self): return self.rel
    def set_rel(self, rel): self.rel = rel
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_tabindex(self): return self.tabindex
    def set_tabindex(self, tabindex): self.tabindex = tabindex
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_Charset(self, value):
        # Validate type Charset, a restriction on xs:string.
        pass
    def validate_LinkTypes(self, value):
        # Validate type LinkTypes, a restriction on xs:NMTOKENS.
        pass
    def validate_LanguageCode(self, value):
        # Validate type LanguageCode, a restriction on xs:language.
        pass
    def validate_Shape(self, value):
        # Validate type Shape, a restriction on xs:token.
        pass
    def validate_URI(self, value):
        # Validate type URI, a restriction on xs:anyURI.
        pass
    def validate_Coords(self, value):
        # Validate type Coords, a restriction on xs:string.
        pass
    def validate_Character(self, value):
        # Validate type Character, a restriction on xs:string.
        pass
    def validate_ContentType(self, value):
        # Validate type ContentType, a restriction on xs:string.
        pass
    def validate_tabindexNumber(self, value):
        # Validate type tabindexNumber, a restriction on Number.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(a, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='a', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='a')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='a', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='a'):
        super(a, self).exportAttributes(outfile, level, already_processed, namespace_, name_='a')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_format_string(quote_attrib(self.name).encode(ExternalEncoding), input_name='name'), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.charset is not None and 'charset' not in already_processed:
            already_processed.add('charset')
            outfile.write(' charset=%s' % (quote_attrib(self.charset), ))
        if self.rev is not None and 'rev' not in already_processed:
            already_processed.add('rev')
            outfile.write(' rev=%s' % (quote_attrib(self.rev), ))
        if self.hreflang is not None and 'hreflang' not in already_processed:
            already_processed.add('hreflang')
            outfile.write(' hreflang=%s' % (quote_attrib(self.hreflang), ))
        if self.shape is not None and 'shape' not in already_processed:
            already_processed.add('shape')
            outfile.write(' shape=%s' % (quote_attrib(self.shape), ))
        if self.href is not None and 'href' not in already_processed:
            already_processed.add('href')
            outfile.write(' href=%s' % (quote_attrib(self.href), ))
        if self.coords is not None and 'coords' not in already_processed:
            already_processed.add('coords')
            outfile.write(' coords=%s' % (quote_attrib(self.coords), ))
        if self.accesskey is not None and 'accesskey' not in already_processed:
            already_processed.add('accesskey')
            outfile.write(' accesskey=%s' % (quote_attrib(self.accesskey), ))
        if self.rel is not None and 'rel' not in already_processed:
            already_processed.add('rel')
            outfile.write(' rel=%s' % (quote_attrib(self.rel), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (quote_attrib(self.type_), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
        if self.tabindex is not None and 'tabindex' not in already_processed:
            already_processed.add('tabindex')
            outfile.write(' tabindex=%s' % (quote_attrib(self.tabindex), ))
    def exportChildren(self, outfile, level, namespace_='', name_='a', fromsubclass_=False, pretty_print=True):
        super(a, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='a', mapping_=None):
        element = super(a, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.name is not None:
            element.set('name', self.gds_format_string(self.name))
        if self.title is not None:
            element.set('title', self.title)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.charset is not None:
            element.set('charset', self.charset)
        if self.rev is not None:
            element.set('rev', self.rev)
        if self.hreflang is not None:
            element.set('hreflang', self.hreflang)
        if self.shape is not None:
            element.set('shape', self.shape)
        if self.href is not None:
            element.set('href', self.href)
        if self.coords is not None:
            element.set('coords', self.coords)
        if self.accesskey is not None:
            element.set('accesskey', self.accesskey)
        if self.rel is not None:
            element.set('rel', self.rel)
        if self.type_ is not None:
            element.set('type', self.type_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if self.tabindex is not None:
            element.set('tabindex', self.tabindex)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('charset', node)
        if value is not None and 'charset' not in already_processed:
            already_processed.add('charset')
            self.charset = value
            self.validate_Charset(self.charset)    # validate type Charset
        value = find_attr_value_('rev', node)
        if value is not None and 'rev' not in already_processed:
            already_processed.add('rev')
            self.rev = value
            self.validate_LinkTypes(self.rev)    # validate type LinkTypes
        value = find_attr_value_('hreflang', node)
        if value is not None and 'hreflang' not in already_processed:
            already_processed.add('hreflang')
            self.hreflang = value
            self.validate_LanguageCode(self.hreflang)    # validate type LanguageCode
        value = find_attr_value_('shape', node)
        if value is not None and 'shape' not in already_processed:
            already_processed.add('shape')
            self.shape = value
            self.shape = ' '.join(self.shape.split())
            self.validate_Shape(self.shape)    # validate type Shape
        value = find_attr_value_('href', node)
        if value is not None and 'href' not in already_processed:
            already_processed.add('href')
            self.href = value
            self.validate_URI(self.href)    # validate type URI
        value = find_attr_value_('coords', node)
        if value is not None and 'coords' not in already_processed:
            already_processed.add('coords')
            self.coords = value
            self.validate_Coords(self.coords)    # validate type Coords
        value = find_attr_value_('accesskey', node)
        if value is not None and 'accesskey' not in already_processed:
            already_processed.add('accesskey')
            self.accesskey = value
            self.validate_Character(self.accesskey)    # validate type Character
        value = find_attr_value_('rel', node)
        if value is not None and 'rel' not in already_processed:
            already_processed.add('rel')
            self.rel = value
            self.validate_LinkTypes(self.rel)    # validate type LinkTypes
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_ContentType(self.type_)    # validate type ContentType
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        value = find_attr_value_('tabindex', node)
        if value is not None and 'tabindex' not in already_processed:
            already_processed.add('tabindex')
            self.tabindex = value
            self.validate_tabindexNumber(self.tabindex)    # validate type tabindexNumber
        super(a, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(a, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class a


class dd(Flow):
    subclass = None
    superclass = Flow
    def __init__(self, p=None, h1=None, h2=None, h3=None, h4=None, h5=None, h6=None, div=None, ul=None, ol=None, dl=None, pre=None, hr=None, blockquote=None, table=None, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(dd, self).__init__(p, h1, h2, h3, h4, h5, h6, div, ul, ol, dl, pre, hr, blockquote, table, a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if dd.subclass:
            return dd.subclass(*args_, **kwargs_)
        else:
            return dd(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(dd, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='dd', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='dd')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='dd', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='dd'):
        super(dd, self).exportAttributes(outfile, level, already_processed, namespace_, name_='dd')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='dd', fromsubclass_=False, pretty_print=True):
        super(dd, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='dd', mapping_=None):
        element = super(dd, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(dd, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(dd, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class dd


class hr(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, title=None, id=None, class_=None, dir=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
    def factory(*args_, **kwargs_):
        if hr.subclass:
            return hr.subclass(*args_, **kwargs_)
        else:
            return hr(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='hr', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='hr')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='hr', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='hr'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='hr', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='hr', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class hr


class pre(pre_content):
    """ content is "Inline" excluding "img|object|big|small|sub|sup" """
    subclass = None
    superclass = pre_content
    def __init__(self, a=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, br=None, span=None, bdo=None, map=None, lang=None, style=None, title=None, space=None, class_=None, id=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(pre, self).__init__(a, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, br, span, bdo, map, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.space = _cast(None, space)
        self.class_ = _cast(None, class_)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
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
        if pre.subclass:
            return pre.subclass(*args_, **kwargs_)
        else:
            return pre(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_space(self): return self.space
    def set_space(self, space): self.space = space
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(pre, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='pre', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='pre')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='pre', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='pre'):
        super(pre, self).exportAttributes(outfile, level, already_processed, namespace_, name_='pre')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.space is not None and 'space' not in already_processed:
            already_processed.add('space')
            outfile.write(' space=%s' % (self.gds_format_string(quote_attrib(self.space).encode(ExternalEncoding), input_name='space'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='pre', fromsubclass_=False, pretty_print=True):
        super(pre, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='pre', mapping_=None):
        element = super(pre, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.space is not None:
            element.set('space', self.gds_format_string(self.space))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('space', node)
        if value is not None and 'space' not in already_processed:
            already_processed.add('space')
            self.space = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(pre, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(pre, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class pre


class blockquote(Block):
    subclass = None
    superclass = Block
    def __init__(self, p=None, h1=None, h2=None, h3=None, h4=None, h5=None, h6=None, div=None, ul=None, ol=None, dl=None, pre=None, hr=None, blockquote_=None, table=None, lang=None, style=None, title=None, class_=None, cite=None, id=None, dir=None):
        self.original_tagname_ = None
        super(blockquote, self).__init__(p, h1, h2, h3, h4, h5, h6, div, ul, ol, dl, pre, hr, blockquote_, table, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.class_ = _cast(None, class_)
        self.cite = _cast(None, cite)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
    def factory(*args_, **kwargs_):
        if blockquote.subclass:
            return blockquote.subclass(*args_, **kwargs_)
        else:
            return blockquote(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_cite(self): return self.cite
    def set_cite(self, cite): self.cite = cite
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_URI(self, value):
        # Validate type URI, a restriction on xs:anyURI.
        pass
    def hasContent_(self):
        if (
            super(blockquote, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='blockquote', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='blockquote')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='blockquote', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='blockquote'):
        super(blockquote, self).exportAttributes(outfile, level, already_processed, namespace_, name_='blockquote')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.cite is not None and 'cite' not in already_processed:
            already_processed.add('cite')
            outfile.write(' cite=%s' % (quote_attrib(self.cite), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='blockquote', fromsubclass_=False, pretty_print=True):
        super(blockquote, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='blockquote', mapping_=None):
        element = super(blockquote, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.cite is not None:
            element.set('cite', self.cite)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('cite', node)
        if value is not None and 'cite' not in already_processed:
            already_processed.add('cite')
            self.cite = value
            self.validate_URI(self.cite)    # validate type URI
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(blockquote, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(blockquote, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class blockquote


class a(a_content):
    """content is "Inline" except that anchors shouldn't be nested"""
    subclass = None
    superclass = a_content
    def __init__(self, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, name=None, title=None, class_=None, charset=None, rev=None, hreflang=None, shape='rect', href=None, coords=None, accesskey=None, rel=None, type_=None, id=None, dir=None, tabindex=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(a, self).__init__(br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.name = _cast(None, name)
        self.title = _cast(None, title)
        self.class_ = _cast(None, class_)
        self.charset = _cast(None, charset)
        self.rev = _cast(None, rev)
        self.hreflang = _cast(None, hreflang)
        self.shape = _cast(None, shape)
        self.href = _cast(None, href)
        self.coords = _cast(None, coords)
        self.accesskey = _cast(None, accesskey)
        self.rel = _cast(None, rel)
        self.type_ = _cast(None, type_)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
        self.tabindex = _cast(None, tabindex)
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
        if a.subclass:
            return a.subclass(*args_, **kwargs_)
        else:
            return a(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_charset(self): return self.charset
    def set_charset(self, charset): self.charset = charset
    def get_rev(self): return self.rev
    def set_rev(self, rev): self.rev = rev
    def get_hreflang(self): return self.hreflang
    def set_hreflang(self, hreflang): self.hreflang = hreflang
    def get_shape(self): return self.shape
    def set_shape(self, shape): self.shape = shape
    def get_href(self): return self.href
    def set_href(self, href): self.href = href
    def get_coords(self): return self.coords
    def set_coords(self, coords): self.coords = coords
    def get_accesskey(self): return self.accesskey
    def set_accesskey(self, accesskey): self.accesskey = accesskey
    def get_rel(self): return self.rel
    def set_rel(self, rel): self.rel = rel
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_tabindex(self): return self.tabindex
    def set_tabindex(self, tabindex): self.tabindex = tabindex
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_Charset(self, value):
        # Validate type Charset, a restriction on xs:string.
        pass
    def validate_LinkTypes(self, value):
        # Validate type LinkTypes, a restriction on xs:NMTOKENS.
        pass
    def validate_LanguageCode(self, value):
        # Validate type LanguageCode, a restriction on xs:language.
        pass
    def validate_Shape(self, value):
        # Validate type Shape, a restriction on xs:token.
        pass
    def validate_URI(self, value):
        # Validate type URI, a restriction on xs:anyURI.
        pass
    def validate_Coords(self, value):
        # Validate type Coords, a restriction on xs:string.
        pass
    def validate_Character(self, value):
        # Validate type Character, a restriction on xs:string.
        pass
    def validate_ContentType(self, value):
        # Validate type ContentType, a restriction on xs:string.
        pass
    def validate_tabindexNumber(self, value):
        # Validate type tabindexNumber, a restriction on Number.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(a, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='a', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='a')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='a', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='a'):
        super(a, self).exportAttributes(outfile, level, already_processed, namespace_, name_='a')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_format_string(quote_attrib(self.name).encode(ExternalEncoding), input_name='name'), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.charset is not None and 'charset' not in already_processed:
            already_processed.add('charset')
            outfile.write(' charset=%s' % (quote_attrib(self.charset), ))
        if self.rev is not None and 'rev' not in already_processed:
            already_processed.add('rev')
            outfile.write(' rev=%s' % (quote_attrib(self.rev), ))
        if self.hreflang is not None and 'hreflang' not in already_processed:
            already_processed.add('hreflang')
            outfile.write(' hreflang=%s' % (quote_attrib(self.hreflang), ))
        if self.shape is not None and 'shape' not in already_processed:
            already_processed.add('shape')
            outfile.write(' shape=%s' % (quote_attrib(self.shape), ))
        if self.href is not None and 'href' not in already_processed:
            already_processed.add('href')
            outfile.write(' href=%s' % (quote_attrib(self.href), ))
        if self.coords is not None and 'coords' not in already_processed:
            already_processed.add('coords')
            outfile.write(' coords=%s' % (quote_attrib(self.coords), ))
        if self.accesskey is not None and 'accesskey' not in already_processed:
            already_processed.add('accesskey')
            outfile.write(' accesskey=%s' % (quote_attrib(self.accesskey), ))
        if self.rel is not None and 'rel' not in already_processed:
            already_processed.add('rel')
            outfile.write(' rel=%s' % (quote_attrib(self.rel), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (quote_attrib(self.type_), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
        if self.tabindex is not None and 'tabindex' not in already_processed:
            already_processed.add('tabindex')
            outfile.write(' tabindex=%s' % (quote_attrib(self.tabindex), ))
    def exportChildren(self, outfile, level, namespace_='', name_='a', fromsubclass_=False, pretty_print=True):
        super(a, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='a', mapping_=None):
        element = super(a, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.name is not None:
            element.set('name', self.gds_format_string(self.name))
        if self.title is not None:
            element.set('title', self.title)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.charset is not None:
            element.set('charset', self.charset)
        if self.rev is not None:
            element.set('rev', self.rev)
        if self.hreflang is not None:
            element.set('hreflang', self.hreflang)
        if self.shape is not None:
            element.set('shape', self.shape)
        if self.href is not None:
            element.set('href', self.href)
        if self.coords is not None:
            element.set('coords', self.coords)
        if self.accesskey is not None:
            element.set('accesskey', self.accesskey)
        if self.rel is not None:
            element.set('rel', self.rel)
        if self.type_ is not None:
            element.set('type', self.type_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if self.tabindex is not None:
            element.set('tabindex', self.tabindex)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('charset', node)
        if value is not None and 'charset' not in already_processed:
            already_processed.add('charset')
            self.charset = value
            self.validate_Charset(self.charset)    # validate type Charset
        value = find_attr_value_('rev', node)
        if value is not None and 'rev' not in already_processed:
            already_processed.add('rev')
            self.rev = value
            self.validate_LinkTypes(self.rev)    # validate type LinkTypes
        value = find_attr_value_('hreflang', node)
        if value is not None and 'hreflang' not in already_processed:
            already_processed.add('hreflang')
            self.hreflang = value
            self.validate_LanguageCode(self.hreflang)    # validate type LanguageCode
        value = find_attr_value_('shape', node)
        if value is not None and 'shape' not in already_processed:
            already_processed.add('shape')
            self.shape = value
            self.shape = ' '.join(self.shape.split())
            self.validate_Shape(self.shape)    # validate type Shape
        value = find_attr_value_('href', node)
        if value is not None and 'href' not in already_processed:
            already_processed.add('href')
            self.href = value
            self.validate_URI(self.href)    # validate type URI
        value = find_attr_value_('coords', node)
        if value is not None and 'coords' not in already_processed:
            already_processed.add('coords')
            self.coords = value
            self.validate_Coords(self.coords)    # validate type Coords
        value = find_attr_value_('accesskey', node)
        if value is not None and 'accesskey' not in already_processed:
            already_processed.add('accesskey')
            self.accesskey = value
            self.validate_Character(self.accesskey)    # validate type Character
        value = find_attr_value_('rel', node)
        if value is not None and 'rel' not in already_processed:
            already_processed.add('rel')
            self.rel = value
            self.validate_LinkTypes(self.rel)    # validate type LinkTypes
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_ContentType(self.type_)    # validate type ContentType
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        value = find_attr_value_('tabindex', node)
        if value is not None and 'tabindex' not in already_processed:
            already_processed.add('tabindex')
            self.tabindex = value
            self.validate_tabindexNumber(self.tabindex)    # validate type tabindexNumber
        super(a, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(a, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class a


class span(Inline):
    """generic language/style container"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span_=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(span, self).__init__(a, br, span_, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if span.subclass:
            return span.subclass(*args_, **kwargs_)
        else:
            return span(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(span, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='span', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='span')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='span', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='span'):
        super(span, self).exportAttributes(outfile, level, already_processed, namespace_, name_='span')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='span', fromsubclass_=False, pretty_print=True):
        super(span, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='span', mapping_=None):
        element = super(span, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(span, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(span, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class span


class bdo(Inline):
    """I18N BiDi over-ride"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo_=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(bdo, self).__init__(a, br, span, bdo_, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if bdo.subclass:
            return bdo.subclass(*args_, **kwargs_)
        else:
            return bdo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(bdo, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='bdo', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='bdo')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='bdo', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='bdo'):
        super(bdo, self).exportAttributes(outfile, level, already_processed, namespace_, name_='bdo')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='bdo', fromsubclass_=False, pretty_print=True):
        super(bdo, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='bdo', mapping_=None):
        element = super(bdo, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(bdo, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(bdo, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class bdo


class br(GeneratedsSuper):
    """forced line break"""
    subclass = None
    superclass = None
    def __init__(self, class_=None, style=None, id=None, title=None):
        self.original_tagname_ = None
        self.class_ = _cast(None, class_)
        self.style = _cast(None, style)
        self.id = _cast(None, id)
        self.title = _cast(None, title)
    def factory(*args_, **kwargs_):
        if br.subclass:
            return br.subclass(*args_, **kwargs_)
        else:
            return br(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='br', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='br')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='br', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='br'):
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
    def exportChildren(self, outfile, level, namespace_='', name_='br', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='br', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.style is not None:
            element.set('style', self.style)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.title is not None:
            element.set('title', self.title)
        if mapping_ is not None:
            mapping_[self] = element
        return element
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class br


class em(Inline):
    """emphasis"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em_=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(em, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em_, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if em.subclass:
            return em.subclass(*args_, **kwargs_)
        else:
            return em(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(em, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='em', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='em')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='em', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='em'):
        super(em, self).exportAttributes(outfile, level, already_processed, namespace_, name_='em')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='em', fromsubclass_=False, pretty_print=True):
        super(em, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='em', mapping_=None):
        element = super(em, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(em, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(em, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class em


class strong(Inline):
    """strong emphasis"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong_=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(strong, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong_, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if strong.subclass:
            return strong.subclass(*args_, **kwargs_)
        else:
            return strong(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(strong, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='strong', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='strong')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='strong', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='strong'):
        super(strong, self).exportAttributes(outfile, level, already_processed, namespace_, name_='strong')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='strong', fromsubclass_=False, pretty_print=True):
        super(strong, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='strong', mapping_=None):
        element = super(strong, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(strong, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(strong, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class strong


class dfn(Inline):
    """definitional"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn_=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(dfn, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn_, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if dfn.subclass:
            return dfn.subclass(*args_, **kwargs_)
        else:
            return dfn(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(dfn, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='dfn', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='dfn')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='dfn', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='dfn'):
        super(dfn, self).exportAttributes(outfile, level, already_processed, namespace_, name_='dfn')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='dfn', fromsubclass_=False, pretty_print=True):
        super(dfn, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='dfn', mapping_=None):
        element = super(dfn, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(dfn, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(dfn, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class dfn


class samp(Inline):
    """sample"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp_=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(samp, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp_, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if samp.subclass:
            return samp.subclass(*args_, **kwargs_)
        else:
            return samp(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(samp, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='samp', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='samp')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='samp', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='samp'):
        super(samp, self).exportAttributes(outfile, level, already_processed, namespace_, name_='samp')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='samp', fromsubclass_=False, pretty_print=True):
        super(samp, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='samp', mapping_=None):
        element = super(samp, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(samp, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(samp, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class samp


class kbd(Inline):
    """something user would type"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd_=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(kbd, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd_, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if kbd.subclass:
            return kbd.subclass(*args_, **kwargs_)
        else:
            return kbd(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(kbd, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='kbd', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='kbd')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='kbd', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='kbd'):
        super(kbd, self).exportAttributes(outfile, level, already_processed, namespace_, name_='kbd')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='kbd', fromsubclass_=False, pretty_print=True):
        super(kbd, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='kbd', mapping_=None):
        element = super(kbd, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(kbd, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(kbd, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class kbd


class var(Inline):
    """variable"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var_=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(var, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var_, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if var.subclass:
            return var.subclass(*args_, **kwargs_)
        else:
            return var(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(var, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='var', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='var')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='var', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='var'):
        super(var, self).exportAttributes(outfile, level, already_processed, namespace_, name_='var')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='var', fromsubclass_=False, pretty_print=True):
        super(var, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='var', mapping_=None):
        element = super(var, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(var, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(var, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class var


class cite(Inline):
    """citation"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite_=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(cite, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite_, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if cite.subclass:
            return cite.subclass(*args_, **kwargs_)
        else:
            return cite(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(cite, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='cite', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='cite')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='cite', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='cite'):
        super(cite, self).exportAttributes(outfile, level, already_processed, namespace_, name_='cite')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='cite', fromsubclass_=False, pretty_print=True):
        super(cite, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='cite', mapping_=None):
        element = super(cite, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(cite, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(cite, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class cite


class abbr(Inline):
    """abbreviation"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr_=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(abbr, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr_, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if abbr.subclass:
            return abbr.subclass(*args_, **kwargs_)
        else:
            return abbr(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(abbr, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='abbr', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='abbr')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='abbr', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='abbr'):
        super(abbr, self).exportAttributes(outfile, level, already_processed, namespace_, name_='abbr')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='abbr', fromsubclass_=False, pretty_print=True):
        super(abbr, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='abbr', mapping_=None):
        element = super(abbr, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(abbr, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(abbr, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class abbr


class acronym(Inline):
    """acronym"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym_=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(acronym, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym_, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if acronym.subclass:
            return acronym.subclass(*args_, **kwargs_)
        else:
            return acronym(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(acronym, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='acronym', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='acronym')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='acronym', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='acronym'):
        super(acronym, self).exportAttributes(outfile, level, already_processed, namespace_, name_='acronym')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='acronym', fromsubclass_=False, pretty_print=True):
        super(acronym, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='acronym', mapping_=None):
        element = super(acronym, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(acronym, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(acronym, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class acronym


class q(Inline):
    """inlined quote"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q_=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, class_=None, cite_attr=None, id=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(q, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q_, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.class_ = _cast(None, class_)
        self.cite_attr = _cast(None, cite_attr)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
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
        if q.subclass:
            return q.subclass(*args_, **kwargs_)
        else:
            return q(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_cite_attr(self): return self.cite_attr
    def set_cite_attr(self, cite_attr): self.cite_attr = cite_attr
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(q, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='q', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='q')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='q', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='q'):
        super(q, self).exportAttributes(outfile, level, already_processed, namespace_, name_='q')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.cite_attr is not None and 'cite_attr' not in already_processed:
            already_processed.add('cite_attr')
            outfile.write(' cite=%s' % (self.gds_format_string(quote_attrib(self.cite_attr).encode(ExternalEncoding), input_name='cite_attr'), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='q', fromsubclass_=False, pretty_print=True):
        super(q, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='q', mapping_=None):
        element = super(q, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.cite_attr is not None:
            element.set('cite_attr', self.gds_format_string(self.cite_attr))
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('cite', node)
        if value is not None and 'cite_attr' not in already_processed:
            already_processed.add('cite_attr')
            self.cite_attr = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(q, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(q, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class q


class sub(Inline):
    """subscript"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub_=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(sub, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub_, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if sub.subclass:
            return sub.subclass(*args_, **kwargs_)
        else:
            return sub(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(sub, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='sub', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='sub')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='sub', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='sub'):
        super(sub, self).exportAttributes(outfile, level, already_processed, namespace_, name_='sub')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='sub', fromsubclass_=False, pretty_print=True):
        super(sub, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='sub', mapping_=None):
        element = super(sub, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(sub, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(sub, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class sub


class sup(Inline):
    """superscript"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup_=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(sup, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup_, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if sup.subclass:
            return sup.subclass(*args_, **kwargs_)
        else:
            return sup(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(sup, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='sup', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='sup')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='sup', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='sup'):
        super(sup, self).exportAttributes(outfile, level, already_processed, namespace_, name_='sup')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='sup', fromsubclass_=False, pretty_print=True):
        super(sup, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='sup', mapping_=None):
        element = super(sup, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(sup, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(sup, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class sup


class tt(Inline):
    """fixed pitch font"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt_=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(tt, self).__init__(a, br, span, bdo, map, img, tt_, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if tt.subclass:
            return tt.subclass(*args_, **kwargs_)
        else:
            return tt(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(tt, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='tt', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='tt')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='tt', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='tt'):
        super(tt, self).exportAttributes(outfile, level, already_processed, namespace_, name_='tt')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='tt', fromsubclass_=False, pretty_print=True):
        super(tt, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='tt', mapping_=None):
        element = super(tt, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(tt, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(tt, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class tt


class i(Inline):
    """italic font"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i_=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(i, self).__init__(a, br, span, bdo, map, img, tt, i_, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if i.subclass:
            return i.subclass(*args_, **kwargs_)
        else:
            return i(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(i, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='i', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='i')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='i', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='i'):
        super(i, self).exportAttributes(outfile, level, already_processed, namespace_, name_='i')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='i', fromsubclass_=False, pretty_print=True):
        super(i, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='i', mapping_=None):
        element = super(i, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(i, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(i, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class i


class b(Inline):
    """bold font"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b_=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(b, self).__init__(a, br, span, bdo, map, img, tt, i, b_, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if b.subclass:
            return b.subclass(*args_, **kwargs_)
        else:
            return b(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(b, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='b', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='b')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='b', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='b'):
        super(b, self).exportAttributes(outfile, level, already_processed, namespace_, name_='b')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='b', fromsubclass_=False, pretty_print=True):
        super(b, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='b', mapping_=None):
        element = super(b, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(b, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(b, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class b


class big(Inline):
    """bigger font"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big_=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(big, self).__init__(a, br, span, bdo, map, img, tt, i, b, big_, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if big.subclass:
            return big.subclass(*args_, **kwargs_)
        else:
            return big(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(big, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='big', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='big')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='big', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='big'):
        super(big, self).exportAttributes(outfile, level, already_processed, namespace_, name_='big')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='big', fromsubclass_=False, pretty_print=True):
        super(big, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='big', mapping_=None):
        element = super(big, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(big, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(big, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class big


class small(Inline):
    """smaller font"""
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small_=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(small, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small_, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if small.subclass:
            return small.subclass(*args_, **kwargs_)
        else:
            return small(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(small, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='small', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='small')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='small', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='small'):
        super(small, self).exportAttributes(outfile, level, already_processed, namespace_, name_='small')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='small', fromsubclass_=False, pretty_print=True):
        super(small, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='small', mapping_=None):
        element = super(small, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(small, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(small, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class small


class img(GeneratedsSuper):
    """usemap points to a map element which may be in this document or an
    external document, although the latter is not widely supported"""
    subclass = None
    superclass = None
    def __init__(self, lang=None, src=None, style=None, title=None, class_=None, height=None, width=None, usemap=None, id=None, alt=None, ismap=None, longdesc=None, dir=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.src = _cast(None, src)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.class_ = _cast(None, class_)
        self.height = _cast(None, height)
        self.width = _cast(None, width)
        self.usemap = _cast(None, usemap)
        self.id = _cast(None, id)
        self.alt = _cast(None, alt)
        self.ismap = _cast(None, ismap)
        self.longdesc = _cast(None, longdesc)
        self.dir = _cast(None, dir)
    def factory(*args_, **kwargs_):
        if img.subclass:
            return img.subclass(*args_, **kwargs_)
        else:
            return img(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_src(self): return self.src
    def set_src(self, src): self.src = src
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_height(self): return self.height
    def set_height(self, height): self.height = height
    def get_width(self): return self.width
    def set_width(self, width): self.width = width
    def get_usemap(self): return self.usemap
    def set_usemap(self, usemap): self.usemap = usemap
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_alt(self): return self.alt
    def set_alt(self, alt): self.alt = alt
    def get_ismap(self): return self.ismap
    def set_ismap(self, ismap): self.ismap = ismap
    def get_longdesc(self): return self.longdesc
    def set_longdesc(self, longdesc): self.longdesc = longdesc
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_URI(self, value):
        # Validate type URI, a restriction on xs:anyURI.
        pass
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_Length(self, value):
        # Validate type Length, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='img', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='img')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='img', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='img'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.src is not None and 'src' not in already_processed:
            already_processed.add('src')
            outfile.write(' src=%s' % (quote_attrib(self.src), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.height is not None and 'height' not in already_processed:
            already_processed.add('height')
            outfile.write(' height=%s' % (quote_attrib(self.height), ))
        if self.width is not None and 'width' not in already_processed:
            already_processed.add('width')
            outfile.write(' width=%s' % (quote_attrib(self.width), ))
        if self.usemap is not None and 'usemap' not in already_processed:
            already_processed.add('usemap')
            outfile.write(' usemap=%s' % (quote_attrib(self.usemap), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.alt is not None and 'alt' not in already_processed:
            already_processed.add('alt')
            outfile.write(' alt=%s' % (quote_attrib(self.alt), ))
        if self.ismap is not None and 'ismap' not in already_processed:
            already_processed.add('ismap')
            outfile.write(' ismap=%s' % (self.gds_format_string(quote_attrib(self.ismap).encode(ExternalEncoding), input_name='ismap'), ))
        if self.longdesc is not None and 'longdesc' not in already_processed:
            already_processed.add('longdesc')
            outfile.write(' longdesc=%s' % (quote_attrib(self.longdesc), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='img', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='img', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.src is not None:
            element.set('src', self.src)
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.height is not None:
            element.set('height', self.height)
        if self.width is not None:
            element.set('width', self.width)
        if self.usemap is not None:
            element.set('usemap', self.usemap)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.alt is not None:
            element.set('alt', self.alt)
        if self.ismap is not None:
            element.set('ismap', self.gds_format_string(self.ismap))
        if self.longdesc is not None:
            element.set('longdesc', self.longdesc)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('src', node)
        if value is not None and 'src' not in already_processed:
            already_processed.add('src')
            self.src = value
            self.validate_URI(self.src)    # validate type URI
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('height', node)
        if value is not None and 'height' not in already_processed:
            already_processed.add('height')
            self.height = value
            self.validate_Length(self.height)    # validate type Length
        value = find_attr_value_('width', node)
        if value is not None and 'width' not in already_processed:
            already_processed.add('width')
            self.width = value
            self.validate_Length(self.width)    # validate type Length
        value = find_attr_value_('usemap', node)
        if value is not None and 'usemap' not in already_processed:
            already_processed.add('usemap')
            self.usemap = value
            self.validate_URI(self.usemap)    # validate type URI
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('alt', node)
        if value is not None and 'alt' not in already_processed:
            already_processed.add('alt')
            self.alt = value
            self.validate_Text(self.alt)    # validate type Text
        value = find_attr_value_('ismap', node)
        if value is not None and 'ismap' not in already_processed:
            already_processed.add('ismap')
            self.ismap = value
            self.ismap = ' '.join(self.ismap.split())
        value = find_attr_value_('longdesc', node)
        if value is not None and 'longdesc' not in already_processed:
            already_processed.add('longdesc')
            self.longdesc = value
            self.validate_URI(self.longdesc)    # validate type URI
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class img


class map(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, name=None, title=None, class_=None, id=None, dir=None, p=None, h1=None, h2=None, h3=None, h4=None, h5=None, h6=None, div=None, ul=None, ol=None, dl=None, pre=None, hr=None, blockquote=None, table=None, area=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.name = _cast(None, name)
        self.title = _cast(None, title)
        self.class_ = _cast(None, class_)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
        self.p = p
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.h5 = h5
        self.h6 = h6
        self.div = div
        self.ul = ul
        self.ol = ol
        self.dl = dl
        self.pre = pre
        self.hr = hr
        self.blockquote = blockquote
        self.table = table
        if area is None:
            self.area = []
        else:
            self.area = area
    def factory(*args_, **kwargs_):
        if map.subclass:
            return map.subclass(*args_, **kwargs_)
        else:
            return list(map(*args_, **kwargs_))
    factory = staticmethod(factory)
    def get_p(self): return self.p
    def set_p(self, p): self.p = p
    def get_h1(self): return self.h1
    def set_h1(self, h1): self.h1 = h1
    def get_h2(self): return self.h2
    def set_h2(self, h2): self.h2 = h2
    def get_h3(self): return self.h3
    def set_h3(self, h3): self.h3 = h3
    def get_h4(self): return self.h4
    def set_h4(self, h4): self.h4 = h4
    def get_h5(self): return self.h5
    def set_h5(self, h5): self.h5 = h5
    def get_h6(self): return self.h6
    def set_h6(self, h6): self.h6 = h6
    def get_div(self): return self.div
    def set_div(self, div): self.div = div
    def get_ul(self): return self.ul
    def set_ul(self, ul): self.ul = ul
    def get_ol(self): return self.ol
    def set_ol(self, ol): self.ol = ol
    def get_dl(self): return self.dl
    def set_dl(self, dl): self.dl = dl
    def get_pre(self): return self.pre
    def set_pre(self, pre): self.pre = pre
    def get_hr(self): return self.hr
    def set_hr(self, hr): self.hr = hr
    def get_blockquote(self): return self.blockquote
    def set_blockquote(self, blockquote): self.blockquote = blockquote
    def get_table(self): return self.table
    def set_table(self, table): self.table = table
    def get_area(self): return self.area
    def set_area(self, area): self.area = area
    def add_area(self, value): self.area.append(value)
    def insert_area(self, index, value): self.area[index] = value
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.p is not None or
            self.h1 is not None or
            self.h2 is not None or
            self.h3 is not None or
            self.h4 is not None or
            self.h5 is not None or
            self.h6 is not None or
            self.div is not None or
            self.ul is not None or
            self.ol is not None or
            self.dl is not None or
            self.pre is not None or
            self.hr is not None or
            self.blockquote is not None or
            self.table is not None or
            self.area
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='map', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='map')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='map', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='map'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_format_string(quote_attrib(self.name).encode(ExternalEncoding), input_name='name'), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (self.gds_format_string(quote_attrib(self.class_).encode(ExternalEncoding), input_name='class'), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='map', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.p is not None:
            self.p.export(outfile, level, namespace_, name_='p', pretty_print=pretty_print)
        if self.h1 is not None:
            self.h1.export(outfile, level, namespace_, name_='h1', pretty_print=pretty_print)
        if self.h2 is not None:
            self.h2.export(outfile, level, namespace_, name_='h2', pretty_print=pretty_print)
        if self.h3 is not None:
            self.h3.export(outfile, level, namespace_, name_='h3', pretty_print=pretty_print)
        if self.h4 is not None:
            self.h4.export(outfile, level, namespace_, name_='h4', pretty_print=pretty_print)
        if self.h5 is not None:
            self.h5.export(outfile, level, namespace_, name_='h5', pretty_print=pretty_print)
        if self.h6 is not None:
            self.h6.export(outfile, level, namespace_, name_='h6', pretty_print=pretty_print)
        if self.div is not None:
            self.div.export(outfile, level, namespace_, name_='div', pretty_print=pretty_print)
        if self.ul is not None:
            self.ul.export(outfile, level, namespace_, name_='ul', pretty_print=pretty_print)
        if self.ol is not None:
            self.ol.export(outfile, level, namespace_, name_='ol', pretty_print=pretty_print)
        if self.dl is not None:
            self.dl.export(outfile, level, namespace_, name_='dl', pretty_print=pretty_print)
        if self.pre is not None:
            self.pre.export(outfile, level, namespace_, name_='pre', pretty_print=pretty_print)
        if self.hr is not None:
            self.hr.export(outfile, level, namespace_, name_='hr', pretty_print=pretty_print)
        if self.blockquote is not None:
            self.blockquote.export(outfile, level, namespace_, name_='blockquote', pretty_print=pretty_print)
        if self.table is not None:
            self.table.export(outfile, level, namespace_, name_='table', pretty_print=pretty_print)
        for area_ in self.area:
            area_.export(outfile, level, namespace_, name_='area', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='map', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.name is not None:
            element.set('name', self.gds_format_string(self.name))
        if self.title is not None:
            element.set('title', self.title)
        if self.class_ is not None:
            element.set('class', self.gds_format_string(self.class_))
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if self.p is not None:
            p_ = self.p
            p_.to_etree(element, name_='p', mapping_=mapping_)
        if self.h1 is not None:
            h1_ = self.h1
            h1_.to_etree(element, name_='h1', mapping_=mapping_)
        if self.h2 is not None:
            h2_ = self.h2
            h2_.to_etree(element, name_='h2', mapping_=mapping_)
        if self.h3 is not None:
            h3_ = self.h3
            h3_.to_etree(element, name_='h3', mapping_=mapping_)
        if self.h4 is not None:
            h4_ = self.h4
            h4_.to_etree(element, name_='h4', mapping_=mapping_)
        if self.h5 is not None:
            h5_ = self.h5
            h5_.to_etree(element, name_='h5', mapping_=mapping_)
        if self.h6 is not None:
            h6_ = self.h6
            h6_.to_etree(element, name_='h6', mapping_=mapping_)
        if self.div is not None:
            div_ = self.div
            div_.to_etree(element, name_='div', mapping_=mapping_)
        if self.ul is not None:
            ul_ = self.ul
            ul_.to_etree(element, name_='ul', mapping_=mapping_)
        if self.ol is not None:
            ol_ = self.ol
            ol_.to_etree(element, name_='ol', mapping_=mapping_)
        if self.dl is not None:
            dl_ = self.dl
            dl_.to_etree(element, name_='dl', mapping_=mapping_)
        if self.pre is not None:
            pre_ = self.pre
            pre_.to_etree(element, name_='pre', mapping_=mapping_)
        if self.hr is not None:
            hr_ = self.hr
            hr_.to_etree(element, name_='hr', mapping_=mapping_)
        if self.blockquote is not None:
            blockquote_ = self.blockquote
            blockquote_.to_etree(element, name_='blockquote', mapping_=mapping_)
        if self.table is not None:
            table_ = self.table
            table_.to_etree(element, name_='table', mapping_=mapping_)
        for area_ in self.area:
            area_.to_etree(element, name_='area', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'p':
            obj_ = p.factory()
            obj_.build(child_)
            self.p = obj_
            obj_.original_tagname_ = 'p'
        elif nodeName_ == 'h1':
            obj_ = h1.factory()
            obj_.build(child_)
            self.h1 = obj_
            obj_.original_tagname_ = 'h1'
        elif nodeName_ == 'h2':
            obj_ = h2.factory()
            obj_.build(child_)
            self.h2 = obj_
            obj_.original_tagname_ = 'h2'
        elif nodeName_ == 'h3':
            obj_ = h3.factory()
            obj_.build(child_)
            self.h3 = obj_
            obj_.original_tagname_ = 'h3'
        elif nodeName_ == 'h4':
            obj_ = h4.factory()
            obj_.build(child_)
            self.h4 = obj_
            obj_.original_tagname_ = 'h4'
        elif nodeName_ == 'h5':
            obj_ = h5.factory()
            obj_.build(child_)
            self.h5 = obj_
            obj_.original_tagname_ = 'h5'
        elif nodeName_ == 'h6':
            obj_ = h6.factory()
            obj_.build(child_)
            self.h6 = obj_
            obj_.original_tagname_ = 'h6'
        elif nodeName_ == 'div':
            obj_ = div.factory()
            obj_.build(child_)
            self.div = obj_
            obj_.original_tagname_ = 'div'
        elif nodeName_ == 'ul':
            obj_ = ul.factory()
            obj_.build(child_)
            self.ul = obj_
            obj_.original_tagname_ = 'ul'
        elif nodeName_ == 'ol':
            obj_ = ol.factory()
            obj_.build(child_)
            self.ol = obj_
            obj_.original_tagname_ = 'ol'
        elif nodeName_ == 'dl':
            obj_ = dl.factory()
            obj_.build(child_)
            self.dl = obj_
            obj_.original_tagname_ = 'dl'
        elif nodeName_ == 'pre':
            obj_ = pre.factory()
            obj_.build(child_)
            self.pre = obj_
            obj_.original_tagname_ = 'pre'
        elif nodeName_ == 'hr':
            obj_ = hr.factory()
            obj_.build(child_)
            self.hr = obj_
            obj_.original_tagname_ = 'hr'
        elif nodeName_ == 'blockquote':
            obj_ = blockquote.factory()
            obj_.build(child_)
            self.blockquote = obj_
            obj_.original_tagname_ = 'blockquote'
        elif nodeName_ == 'table':
            obj_ = table.factory()
            obj_.build(child_)
            self.table = obj_
            obj_.original_tagname_ = 'table'
        elif nodeName_ == 'area':
            obj_ = area.factory()
            obj_.build(child_)
            self.area.append(obj_)
            obj_.original_tagname_ = 'area'
# end class map


class area(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, title=None, accesskey=None, class_=None, nohref=None, shape='rect', href=None, coords=None, alt=None, id=None, dir=None, tabindex=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.accesskey = _cast(None, accesskey)
        self.class_ = _cast(None, class_)
        self.nohref = _cast(None, nohref)
        self.shape = _cast(None, shape)
        self.href = _cast(None, href)
        self.coords = _cast(None, coords)
        self.alt = _cast(None, alt)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
        self.tabindex = _cast(None, tabindex)
    def factory(*args_, **kwargs_):
        if area.subclass:
            return area.subclass(*args_, **kwargs_)
        else:
            return area(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_accesskey(self): return self.accesskey
    def set_accesskey(self, accesskey): self.accesskey = accesskey
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_nohref(self): return self.nohref
    def set_nohref(self, nohref): self.nohref = nohref
    def get_shape(self): return self.shape
    def set_shape(self, shape): self.shape = shape
    def get_href(self): return self.href
    def set_href(self, href): self.href = href
    def get_coords(self): return self.coords
    def set_coords(self, coords): self.coords = coords
    def get_alt(self): return self.alt
    def set_alt(self, alt): self.alt = alt
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_tabindex(self): return self.tabindex
    def set_tabindex(self, tabindex): self.tabindex = tabindex
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_Character(self, value):
        # Validate type Character, a restriction on xs:string.
        pass
    def validate_Shape(self, value):
        # Validate type Shape, a restriction on xs:token.
        pass
    def validate_URI(self, value):
        # Validate type URI, a restriction on xs:anyURI.
        pass
    def validate_Coords(self, value):
        # Validate type Coords, a restriction on xs:string.
        pass
    def validate_tabindexNumber(self, value):
        # Validate type tabindexNumber, a restriction on Number.
        pass
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='area', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='area')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='area', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='area'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.accesskey is not None and 'accesskey' not in already_processed:
            already_processed.add('accesskey')
            outfile.write(' accesskey=%s' % (quote_attrib(self.accesskey), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.nohref is not None and 'nohref' not in already_processed:
            already_processed.add('nohref')
            outfile.write(' nohref=%s' % (self.gds_format_string(quote_attrib(self.nohref).encode(ExternalEncoding), input_name='nohref'), ))
        if self.shape is not None and 'shape' not in already_processed:
            already_processed.add('shape')
            outfile.write(' shape=%s' % (quote_attrib(self.shape), ))
        if self.href is not None and 'href' not in already_processed:
            already_processed.add('href')
            outfile.write(' href=%s' % (quote_attrib(self.href), ))
        if self.coords is not None and 'coords' not in already_processed:
            already_processed.add('coords')
            outfile.write(' coords=%s' % (quote_attrib(self.coords), ))
        if self.alt is not None and 'alt' not in already_processed:
            already_processed.add('alt')
            outfile.write(' alt=%s' % (quote_attrib(self.alt), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
        if self.tabindex is not None and 'tabindex' not in already_processed:
            already_processed.add('tabindex')
            outfile.write(' tabindex=%s' % (quote_attrib(self.tabindex), ))
    def exportChildren(self, outfile, level, namespace_='', name_='area', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='area', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.accesskey is not None:
            element.set('accesskey', self.accesskey)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.nohref is not None:
            element.set('nohref', self.gds_format_string(self.nohref))
        if self.shape is not None:
            element.set('shape', self.shape)
        if self.href is not None:
            element.set('href', self.href)
        if self.coords is not None:
            element.set('coords', self.coords)
        if self.alt is not None:
            element.set('alt', self.alt)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if self.tabindex is not None:
            element.set('tabindex', self.tabindex)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('accesskey', node)
        if value is not None and 'accesskey' not in already_processed:
            already_processed.add('accesskey')
            self.accesskey = value
            self.validate_Character(self.accesskey)    # validate type Character
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('nohref', node)
        if value is not None and 'nohref' not in already_processed:
            already_processed.add('nohref')
            self.nohref = value
            self.nohref = ' '.join(self.nohref.split())
        value = find_attr_value_('shape', node)
        if value is not None and 'shape' not in already_processed:
            already_processed.add('shape')
            self.shape = value
            self.shape = ' '.join(self.shape.split())
            self.validate_Shape(self.shape)    # validate type Shape
        value = find_attr_value_('href', node)
        if value is not None and 'href' not in already_processed:
            already_processed.add('href')
            self.href = value
            self.validate_URI(self.href)    # validate type URI
        value = find_attr_value_('coords', node)
        if value is not None and 'coords' not in already_processed:
            already_processed.add('coords')
            self.coords = value
            self.validate_Coords(self.coords)    # validate type Coords
        value = find_attr_value_('alt', node)
        if value is not None and 'alt' not in already_processed:
            already_processed.add('alt')
            self.alt = value
            self.validate_Text(self.alt)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        value = find_attr_value_('tabindex', node)
        if value is not None and 'tabindex' not in already_processed:
            already_processed.add('tabindex')
            self.tabindex = value
            self.validate_tabindexNumber(self.tabindex)    # validate type tabindexNumber
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class area


class table(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, title=None, rules=None, border=None, frame=None, summary=None, width=None, class_=None, cellpadding=None, cellspacing=None, id=None, dir=None, caption=None, col=None, colgroup=None, thead=None, tfoot=None, tbody=None, tr=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.rules = _cast(None, rules)
        self.border = _cast(None, border)
        self.frame = _cast(None, frame)
        self.summary = _cast(None, summary)
        self.width = _cast(None, width)
        self.class_ = _cast(None, class_)
        self.cellpadding = _cast(None, cellpadding)
        self.cellspacing = _cast(None, cellspacing)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
        self.caption = caption
        if col is None:
            self.col = []
        else:
            self.col = col
        if colgroup is None:
            self.colgroup = []
        else:
            self.colgroup = colgroup
        self.thead = thead
        self.tfoot = tfoot
        if tbody is None:
            self.tbody = []
        else:
            self.tbody = tbody
        if tr is None:
            self.tr = []
        else:
            self.tr = tr
    def factory(*args_, **kwargs_):
        if table.subclass:
            return table.subclass(*args_, **kwargs_)
        else:
            return table(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_caption(self): return self.caption
    def set_caption(self, caption): self.caption = caption
    def get_col(self): return self.col
    def set_col(self, col): self.col = col
    def add_col(self, value): self.col.append(value)
    def insert_col(self, index, value): self.col[index] = value
    def get_colgroup(self): return self.colgroup
    def set_colgroup(self, colgroup): self.colgroup = colgroup
    def add_colgroup(self, value): self.colgroup.append(value)
    def insert_colgroup(self, index, value): self.colgroup[index] = value
    def get_thead(self): return self.thead
    def set_thead(self, thead): self.thead = thead
    def get_tfoot(self): return self.tfoot
    def set_tfoot(self, tfoot): self.tfoot = tfoot
    def get_tbody(self): return self.tbody
    def set_tbody(self, tbody): self.tbody = tbody
    def add_tbody(self, value): self.tbody.append(value)
    def insert_tbody(self, index, value): self.tbody[index] = value
    def get_tr(self): return self.tr
    def set_tr(self, tr): self.tr = tr
    def add_tr(self, value): self.tr.append(value)
    def insert_tr(self, index, value): self.tr[index] = value
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_rules(self): return self.rules
    def set_rules(self, rules): self.rules = rules
    def get_border(self): return self.border
    def set_border(self, border): self.border = border
    def get_frame(self): return self.frame
    def set_frame(self, frame): self.frame = frame
    def get_summary(self): return self.summary
    def set_summary(self, summary): self.summary = summary
    def get_width(self): return self.width
    def set_width(self, width): self.width = width
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_cellpadding(self): return self.cellpadding
    def set_cellpadding(self, cellpadding): self.cellpadding = cellpadding
    def get_cellspacing(self): return self.cellspacing
    def set_cellspacing(self, cellspacing): self.cellspacing = cellspacing
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_TRules(self, value):
        # Validate type TRules, a restriction on xs:token.
        pass
    def validate_Pixels(self, value):
        # Validate type Pixels, a restriction on xs:nonNegativeInteger.
        pass
    def validate_TFrame(self, value):
        # Validate type TFrame, a restriction on xs:token.
        pass
    def validate_Length(self, value):
        # Validate type Length, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.caption is not None or
            self.col or
            self.colgroup or
            self.thead is not None or
            self.tfoot is not None or
            self.tbody or
            self.tr
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='table', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='table')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='table', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='table'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.rules is not None and 'rules' not in already_processed:
            already_processed.add('rules')
            outfile.write(' rules=%s' % (quote_attrib(self.rules), ))
        if self.border is not None and 'border' not in already_processed:
            already_processed.add('border')
            outfile.write(' border=%s' % (quote_attrib(self.border), ))
        if self.frame is not None and 'frame' not in already_processed:
            already_processed.add('frame')
            outfile.write(' frame=%s' % (quote_attrib(self.frame), ))
        if self.summary is not None and 'summary' not in already_processed:
            already_processed.add('summary')
            outfile.write(' summary=%s' % (quote_attrib(self.summary), ))
        if self.width is not None and 'width' not in already_processed:
            already_processed.add('width')
            outfile.write(' width=%s' % (quote_attrib(self.width), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.cellpadding is not None and 'cellpadding' not in already_processed:
            already_processed.add('cellpadding')
            outfile.write(' cellpadding=%s' % (quote_attrib(self.cellpadding), ))
        if self.cellspacing is not None and 'cellspacing' not in already_processed:
            already_processed.add('cellspacing')
            outfile.write(' cellspacing=%s' % (quote_attrib(self.cellspacing), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='table', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.caption is not None:
            self.caption.export(outfile, level, namespace_, name_='caption', pretty_print=pretty_print)
        for col_ in self.col:
            col_.export(outfile, level, namespace_, name_='col', pretty_print=pretty_print)
        for colgroup_ in self.colgroup:
            colgroup_.export(outfile, level, namespace_, name_='colgroup', pretty_print=pretty_print)
        if self.thead is not None:
            self.thead.export(outfile, level, namespace_, name_='thead', pretty_print=pretty_print)
        if self.tfoot is not None:
            self.tfoot.export(outfile, level, namespace_, name_='tfoot', pretty_print=pretty_print)
        for tbody_ in self.tbody:
            tbody_.export(outfile, level, namespace_, name_='tbody', pretty_print=pretty_print)
        for tr_ in self.tr:
            tr_.export(outfile, level, namespace_, name_='tr', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='table', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.rules is not None:
            element.set('rules', self.rules)
        if self.border is not None:
            element.set('border', self.border)
        if self.frame is not None:
            element.set('frame', self.frame)
        if self.summary is not None:
            element.set('summary', self.summary)
        if self.width is not None:
            element.set('width', self.width)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.cellpadding is not None:
            element.set('cellpadding', self.cellpadding)
        if self.cellspacing is not None:
            element.set('cellspacing', self.cellspacing)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if self.caption is not None:
            caption_ = self.caption
            caption_.to_etree(element, name_='caption', mapping_=mapping_)
        for col_ in self.col:
            col_.to_etree(element, name_='col', mapping_=mapping_)
        for colgroup_ in self.colgroup:
            colgroup_.to_etree(element, name_='colgroup', mapping_=mapping_)
        if self.thead is not None:
            thead_ = self.thead
            thead_.to_etree(element, name_='thead', mapping_=mapping_)
        if self.tfoot is not None:
            tfoot_ = self.tfoot
            tfoot_.to_etree(element, name_='tfoot', mapping_=mapping_)
        for tbody_ in self.tbody:
            tbody_.to_etree(element, name_='tbody', mapping_=mapping_)
        for tr_ in self.tr:
            tr_.to_etree(element, name_='tr', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('rules', node)
        if value is not None and 'rules' not in already_processed:
            already_processed.add('rules')
            self.rules = value
            self.rules = ' '.join(self.rules.split())
            self.validate_TRules(self.rules)    # validate type TRules
        value = find_attr_value_('border', node)
        if value is not None and 'border' not in already_processed:
            already_processed.add('border')
            try:
                self.border = int(value)
            except ValueError as exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
            if self.border < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
            self.validate_Pixels(self.border)    # validate type Pixels
        value = find_attr_value_('frame', node)
        if value is not None and 'frame' not in already_processed:
            already_processed.add('frame')
            self.frame = value
            self.frame = ' '.join(self.frame.split())
            self.validate_TFrame(self.frame)    # validate type TFrame
        value = find_attr_value_('summary', node)
        if value is not None and 'summary' not in already_processed:
            already_processed.add('summary')
            self.summary = value
            self.validate_Text(self.summary)    # validate type Text
        value = find_attr_value_('width', node)
        if value is not None and 'width' not in already_processed:
            already_processed.add('width')
            self.width = value
            self.validate_Length(self.width)    # validate type Length
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('cellpadding', node)
        if value is not None and 'cellpadding' not in already_processed:
            already_processed.add('cellpadding')
            self.cellpadding = value
            self.validate_Length(self.cellpadding)    # validate type Length
        value = find_attr_value_('cellspacing', node)
        if value is not None and 'cellspacing' not in already_processed:
            already_processed.add('cellspacing')
            self.cellspacing = value
            self.validate_Length(self.cellspacing)    # validate type Length
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'caption':
            obj_ = caption.factory()
            obj_.build(child_)
            self.caption = obj_
            obj_.original_tagname_ = 'caption'
        elif nodeName_ == 'col':
            obj_ = col.factory()
            obj_.build(child_)
            self.col.append(obj_)
            obj_.original_tagname_ = 'col'
        elif nodeName_ == 'colgroup':
            obj_ = colgroup.factory()
            obj_.build(child_)
            self.colgroup.append(obj_)
            obj_.original_tagname_ = 'colgroup'
        elif nodeName_ == 'thead':
            obj_ = thead.factory()
            obj_.build(child_)
            self.thead = obj_
            obj_.original_tagname_ = 'thead'
        elif nodeName_ == 'tfoot':
            obj_ = tfoot.factory()
            obj_.build(child_)
            self.tfoot = obj_
            obj_.original_tagname_ = 'tfoot'
        elif nodeName_ == 'tbody':
            obj_ = tbody.factory()
            obj_.build(child_)
            self.tbody.append(obj_)
            obj_.original_tagname_ = 'tbody'
        elif nodeName_ == 'tr':
            obj_ = tr.factory()
            obj_.build(child_)
            self.tr.append(obj_)
            obj_.original_tagname_ = 'tr'
# end class table


class caption(Inline):
    subclass = None
    superclass = Inline
    def __init__(self, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, title=None, id=None, class_=None, dir=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(caption, self).__init__(a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.id = _cast(None, id)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
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
        if caption.subclass:
            return caption.subclass(*args_, **kwargs_)
        else:
            return caption(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(caption, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='caption', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='caption')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='caption', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='caption'):
        super(caption, self).exportAttributes(outfile, level, already_processed, namespace_, name_='caption')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='caption', fromsubclass_=False, pretty_print=True):
        super(caption, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='caption', mapping_=None):
        element = super(caption, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        super(caption, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(caption, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class caption


class thead(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, title=None, align=None, id=None, char=None, valign=None, charoff=None, class_=None, dir=None, tr=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.align = _cast(None, align)
        self.id = _cast(None, id)
        self.char = _cast(None, char)
        self.valign = _cast(None, valign)
        self.charoff = _cast(None, charoff)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
        if tr is None:
            self.tr = []
        else:
            self.tr = tr
    def factory(*args_, **kwargs_):
        if thead.subclass:
            return thead.subclass(*args_, **kwargs_)
        else:
            return thead(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_tr(self): return self.tr
    def set_tr(self, tr): self.tr = tr
    def add_tr(self, value): self.tr.append(value)
    def insert_tr(self, index, value): self.tr[index] = value
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_align(self): return self.align
    def set_align(self, align): self.align = align
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_char(self): return self.char
    def set_char(self, char): self.char = char
    def get_valign(self): return self.valign
    def set_valign(self, valign): self.valign = valign
    def get_charoff(self): return self.charoff
    def set_charoff(self, charoff): self.charoff = charoff
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_Character(self, value):
        # Validate type Character, a restriction on xs:string.
        pass
    def validate_Length(self, value):
        # Validate type Length, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.tr
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='thead', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='thead')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='thead', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='thead'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.align is not None and 'align' not in already_processed:
            already_processed.add('align')
            outfile.write(' align=%s' % (self.gds_format_string(quote_attrib(self.align).encode(ExternalEncoding), input_name='align'), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.char is not None and 'char' not in already_processed:
            already_processed.add('char')
            outfile.write(' char=%s' % (quote_attrib(self.char), ))
        if self.valign is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            outfile.write(' valign=%s' % (self.gds_format_string(quote_attrib(self.valign).encode(ExternalEncoding), input_name='valign'), ))
        if self.charoff is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            outfile.write(' charoff=%s' % (quote_attrib(self.charoff), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='thead', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for tr_ in self.tr:
            tr_.export(outfile, level, namespace_, name_='tr', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='thead', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.align is not None:
            element.set('align', self.gds_format_string(self.align))
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.char is not None:
            element.set('char', self.char)
        if self.valign is not None:
            element.set('valign', self.gds_format_string(self.valign))
        if self.charoff is not None:
            element.set('charoff', self.charoff)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        for tr_ in self.tr:
            tr_.to_etree(element, name_='tr', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('align', node)
        if value is not None and 'align' not in already_processed:
            already_processed.add('align')
            self.align = value
            self.align = ' '.join(self.align.split())
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('char', node)
        if value is not None and 'char' not in already_processed:
            already_processed.add('char')
            self.char = value
            self.validate_Character(self.char)    # validate type Character
        value = find_attr_value_('valign', node)
        if value is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            self.valign = value
            self.valign = ' '.join(self.valign.split())
        value = find_attr_value_('charoff', node)
        if value is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            self.charoff = value
            self.validate_Length(self.charoff)    # validate type Length
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'tr':
            obj_ = tr.factory()
            obj_.build(child_)
            self.tr.append(obj_)
            obj_.original_tagname_ = 'tr'
# end class thead


class tfoot(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, title=None, align=None, id=None, char=None, valign=None, charoff=None, class_=None, dir=None, tr=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.align = _cast(None, align)
        self.id = _cast(None, id)
        self.char = _cast(None, char)
        self.valign = _cast(None, valign)
        self.charoff = _cast(None, charoff)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
        if tr is None:
            self.tr = []
        else:
            self.tr = tr
    def factory(*args_, **kwargs_):
        if tfoot.subclass:
            return tfoot.subclass(*args_, **kwargs_)
        else:
            return tfoot(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_tr(self): return self.tr
    def set_tr(self, tr): self.tr = tr
    def add_tr(self, value): self.tr.append(value)
    def insert_tr(self, index, value): self.tr[index] = value
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_align(self): return self.align
    def set_align(self, align): self.align = align
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_char(self): return self.char
    def set_char(self, char): self.char = char
    def get_valign(self): return self.valign
    def set_valign(self, valign): self.valign = valign
    def get_charoff(self): return self.charoff
    def set_charoff(self, charoff): self.charoff = charoff
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_Character(self, value):
        # Validate type Character, a restriction on xs:string.
        pass
    def validate_Length(self, value):
        # Validate type Length, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.tr
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='tfoot', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='tfoot')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='tfoot', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='tfoot'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.align is not None and 'align' not in already_processed:
            already_processed.add('align')
            outfile.write(' align=%s' % (self.gds_format_string(quote_attrib(self.align).encode(ExternalEncoding), input_name='align'), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.char is not None and 'char' not in already_processed:
            already_processed.add('char')
            outfile.write(' char=%s' % (quote_attrib(self.char), ))
        if self.valign is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            outfile.write(' valign=%s' % (self.gds_format_string(quote_attrib(self.valign).encode(ExternalEncoding), input_name='valign'), ))
        if self.charoff is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            outfile.write(' charoff=%s' % (quote_attrib(self.charoff), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='tfoot', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for tr_ in self.tr:
            tr_.export(outfile, level, namespace_, name_='tr', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='tfoot', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.align is not None:
            element.set('align', self.gds_format_string(self.align))
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.char is not None:
            element.set('char', self.char)
        if self.valign is not None:
            element.set('valign', self.gds_format_string(self.valign))
        if self.charoff is not None:
            element.set('charoff', self.charoff)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        for tr_ in self.tr:
            tr_.to_etree(element, name_='tr', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('align', node)
        if value is not None and 'align' not in already_processed:
            already_processed.add('align')
            self.align = value
            self.align = ' '.join(self.align.split())
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('char', node)
        if value is not None and 'char' not in already_processed:
            already_processed.add('char')
            self.char = value
            self.validate_Character(self.char)    # validate type Character
        value = find_attr_value_('valign', node)
        if value is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            self.valign = value
            self.valign = ' '.join(self.valign.split())
        value = find_attr_value_('charoff', node)
        if value is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            self.charoff = value
            self.validate_Length(self.charoff)    # validate type Length
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'tr':
            obj_ = tr.factory()
            obj_.build(child_)
            self.tr.append(obj_)
            obj_.original_tagname_ = 'tr'
# end class tfoot


class tbody(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, title=None, align=None, id=None, char=None, valign=None, charoff=None, class_=None, dir=None, tr=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.align = _cast(None, align)
        self.id = _cast(None, id)
        self.char = _cast(None, char)
        self.valign = _cast(None, valign)
        self.charoff = _cast(None, charoff)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
        if tr is None:
            self.tr = []
        else:
            self.tr = tr
    def factory(*args_, **kwargs_):
        if tbody.subclass:
            return tbody.subclass(*args_, **kwargs_)
        else:
            return tbody(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_tr(self): return self.tr
    def set_tr(self, tr): self.tr = tr
    def add_tr(self, value): self.tr.append(value)
    def insert_tr(self, index, value): self.tr[index] = value
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_align(self): return self.align
    def set_align(self, align): self.align = align
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_char(self): return self.char
    def set_char(self, char): self.char = char
    def get_valign(self): return self.valign
    def set_valign(self, valign): self.valign = valign
    def get_charoff(self): return self.charoff
    def set_charoff(self, charoff): self.charoff = charoff
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_Character(self, value):
        # Validate type Character, a restriction on xs:string.
        pass
    def validate_Length(self, value):
        # Validate type Length, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.tr
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='tbody', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='tbody')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='tbody', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='tbody'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.align is not None and 'align' not in already_processed:
            already_processed.add('align')
            outfile.write(' align=%s' % (self.gds_format_string(quote_attrib(self.align).encode(ExternalEncoding), input_name='align'), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.char is not None and 'char' not in already_processed:
            already_processed.add('char')
            outfile.write(' char=%s' % (quote_attrib(self.char), ))
        if self.valign is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            outfile.write(' valign=%s' % (self.gds_format_string(quote_attrib(self.valign).encode(ExternalEncoding), input_name='valign'), ))
        if self.charoff is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            outfile.write(' charoff=%s' % (quote_attrib(self.charoff), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='tbody', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for tr_ in self.tr:
            tr_.export(outfile, level, namespace_, name_='tr', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='tbody', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.align is not None:
            element.set('align', self.gds_format_string(self.align))
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.char is not None:
            element.set('char', self.char)
        if self.valign is not None:
            element.set('valign', self.gds_format_string(self.valign))
        if self.charoff is not None:
            element.set('charoff', self.charoff)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        for tr_ in self.tr:
            tr_.to_etree(element, name_='tr', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('align', node)
        if value is not None and 'align' not in already_processed:
            already_processed.add('align')
            self.align = value
            self.align = ' '.join(self.align.split())
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('char', node)
        if value is not None and 'char' not in already_processed:
            already_processed.add('char')
            self.char = value
            self.validate_Character(self.char)    # validate type Character
        value = find_attr_value_('valign', node)
        if value is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            self.valign = value
            self.valign = ' '.join(self.valign.split())
        value = find_attr_value_('charoff', node)
        if value is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            self.charoff = value
            self.validate_Length(self.charoff)    # validate type Length
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'tr':
            obj_ = tr.factory()
            obj_.build(child_)
            self.tr.append(obj_)
            obj_.original_tagname_ = 'tr'
# end class tbody


class colgroup(GeneratedsSuper):
    """colgroup groups a set of col elements. It allows you to group
    several semantically related columns together."""
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, span='1', title=None, align=None, class_=None, char=None, width=None, valign=None, charoff=None, id=None, dir=None, col=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.span = _cast(None, span)
        self.title = _cast(None, title)
        self.align = _cast(None, align)
        self.class_ = _cast(None, class_)
        self.char = _cast(None, char)
        self.width = _cast(None, width)
        self.valign = _cast(None, valign)
        self.charoff = _cast(None, charoff)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
        if col is None:
            self.col = []
        else:
            self.col = col
    def factory(*args_, **kwargs_):
        if colgroup.subclass:
            return colgroup.subclass(*args_, **kwargs_)
        else:
            return colgroup(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_col(self): return self.col
    def set_col(self, col): self.col = col
    def add_col(self, value): self.col.append(value)
    def insert_col(self, index, value): self.col[index] = value
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_span(self): return self.span
    def set_span(self, span): self.span = span
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_align(self): return self.align
    def set_align(self, align): self.align = align
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_char(self): return self.char
    def set_char(self, char): self.char = char
    def get_width(self): return self.width
    def set_width(self, width): self.width = width
    def get_valign(self): return self.valign
    def set_valign(self, valign): self.valign = valign
    def get_charoff(self): return self.charoff
    def set_charoff(self, charoff): self.charoff = charoff
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Number(self, value):
        # Validate type Number, a restriction on xs:nonNegativeInteger.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_Character(self, value):
        # Validate type Character, a restriction on xs:string.
        pass
    def validate_MultiLength(self, value):
        # Validate type MultiLength, a restriction on xs:string.
        pass
    def validate_Length(self, value):
        # Validate type Length, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.col
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='colgroup', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='colgroup')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='colgroup', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='colgroup'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.span is not None and 'span' not in already_processed:
            already_processed.add('span')
            outfile.write(' span=%s' % (quote_attrib(self.span), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.align is not None and 'align' not in already_processed:
            already_processed.add('align')
            outfile.write(' align=%s' % (self.gds_format_string(quote_attrib(self.align).encode(ExternalEncoding), input_name='align'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.char is not None and 'char' not in already_processed:
            already_processed.add('char')
            outfile.write(' char=%s' % (quote_attrib(self.char), ))
        if self.width is not None and 'width' not in already_processed:
            already_processed.add('width')
            outfile.write(' width=%s' % (quote_attrib(self.width), ))
        if self.valign is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            outfile.write(' valign=%s' % (self.gds_format_string(quote_attrib(self.valign).encode(ExternalEncoding), input_name='valign'), ))
        if self.charoff is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            outfile.write(' charoff=%s' % (quote_attrib(self.charoff), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='colgroup', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for col_ in self.col:
            col_.export(outfile, level, namespace_, name_='col', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='colgroup', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.span is not None:
            element.set('span', self.span)
        if self.title is not None:
            element.set('title', self.title)
        if self.align is not None:
            element.set('align', self.gds_format_string(self.align))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.char is not None:
            element.set('char', self.char)
        if self.width is not None:
            element.set('width', self.width)
        if self.valign is not None:
            element.set('valign', self.gds_format_string(self.valign))
        if self.charoff is not None:
            element.set('charoff', self.charoff)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        for col_ in self.col:
            col_.to_etree(element, name_='col', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('span', node)
        if value is not None and 'span' not in already_processed:
            already_processed.add('span')
            try:
                self.span = int(value)
            except ValueError as exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
            if self.span < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
            self.validate_Number(self.span)    # validate type Number
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('align', node)
        if value is not None and 'align' not in already_processed:
            already_processed.add('align')
            self.align = value
            self.align = ' '.join(self.align.split())
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('char', node)
        if value is not None and 'char' not in already_processed:
            already_processed.add('char')
            self.char = value
            self.validate_Character(self.char)    # validate type Character
        value = find_attr_value_('width', node)
        if value is not None and 'width' not in already_processed:
            already_processed.add('width')
            self.width = value
            self.validate_MultiLength(self.width)    # validate type MultiLength
        value = find_attr_value_('valign', node)
        if value is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            self.valign = value
            self.valign = ' '.join(self.valign.split())
        value = find_attr_value_('charoff', node)
        if value is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            self.charoff = value
            self.validate_Length(self.charoff)    # validate type Length
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'col':
            obj_ = col.factory()
            obj_.build(child_)
            self.col.append(obj_)
            obj_.original_tagname_ = 'col'
# end class colgroup


class col(GeneratedsSuper):
    """col elements define the alignment properties for cells in one or
    more columns. The width attribute specifies the width of the
    columns, e.g. width=64 width in screen pixels width=0.5*
    relative width of 0.5 The span attribute causes the attributes
    of one col element to apply to more than one column."""
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, span='1', title=None, align=None, class_=None, char=None, width=None, valign=None, charoff=None, id=None, dir=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.span = _cast(None, span)
        self.title = _cast(None, title)
        self.align = _cast(None, align)
        self.class_ = _cast(None, class_)
        self.char = _cast(None, char)
        self.width = _cast(None, width)
        self.valign = _cast(None, valign)
        self.charoff = _cast(None, charoff)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
    def factory(*args_, **kwargs_):
        if col.subclass:
            return col.subclass(*args_, **kwargs_)
        else:
            return col(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_span(self): return self.span
    def set_span(self, span): self.span = span
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_align(self): return self.align
    def set_align(self, align): self.align = align
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_char(self): return self.char
    def set_char(self, char): self.char = char
    def get_width(self): return self.width
    def set_width(self, width): self.width = width
    def get_valign(self): return self.valign
    def set_valign(self, valign): self.valign = valign
    def get_charoff(self): return self.charoff
    def set_charoff(self, charoff): self.charoff = charoff
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Number(self, value):
        # Validate type Number, a restriction on xs:nonNegativeInteger.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_Character(self, value):
        # Validate type Character, a restriction on xs:string.
        pass
    def validate_MultiLength(self, value):
        # Validate type MultiLength, a restriction on xs:string.
        pass
    def validate_Length(self, value):
        # Validate type Length, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='col', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='col')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='col', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='col'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.span is not None and 'span' not in already_processed:
            already_processed.add('span')
            outfile.write(' span=%s' % (quote_attrib(self.span), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.align is not None and 'align' not in already_processed:
            already_processed.add('align')
            outfile.write(' align=%s' % (self.gds_format_string(quote_attrib(self.align).encode(ExternalEncoding), input_name='align'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.char is not None and 'char' not in already_processed:
            already_processed.add('char')
            outfile.write(' char=%s' % (quote_attrib(self.char), ))
        if self.width is not None and 'width' not in already_processed:
            already_processed.add('width')
            outfile.write(' width=%s' % (quote_attrib(self.width), ))
        if self.valign is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            outfile.write(' valign=%s' % (self.gds_format_string(quote_attrib(self.valign).encode(ExternalEncoding), input_name='valign'), ))
        if self.charoff is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            outfile.write(' charoff=%s' % (quote_attrib(self.charoff), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='col', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='col', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.span is not None:
            element.set('span', self.span)
        if self.title is not None:
            element.set('title', self.title)
        if self.align is not None:
            element.set('align', self.gds_format_string(self.align))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.char is not None:
            element.set('char', self.char)
        if self.width is not None:
            element.set('width', self.width)
        if self.valign is not None:
            element.set('valign', self.gds_format_string(self.valign))
        if self.charoff is not None:
            element.set('charoff', self.charoff)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('span', node)
        if value is not None and 'span' not in already_processed:
            already_processed.add('span')
            try:
                self.span = int(value)
            except ValueError as exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
            if self.span < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
            self.validate_Number(self.span)    # validate type Number
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('align', node)
        if value is not None and 'align' not in already_processed:
            already_processed.add('align')
            self.align = value
            self.align = ' '.join(self.align.split())
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('char', node)
        if value is not None and 'char' not in already_processed:
            already_processed.add('char')
            self.char = value
            self.validate_Character(self.char)    # validate type Character
        value = find_attr_value_('width', node)
        if value is not None and 'width' not in already_processed:
            already_processed.add('width')
            self.width = value
            self.validate_MultiLength(self.width)    # validate type MultiLength
        value = find_attr_value_('valign', node)
        if value is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            self.valign = value
            self.valign = ' '.join(self.valign.split())
        value = find_attr_value_('charoff', node)
        if value is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            self.charoff = value
            self.validate_Length(self.charoff)    # validate type Length
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class col


class tr(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, lang=None, style=None, title=None, align=None, id=None, char=None, valign=None, charoff=None, class_=None, dir=None, th=None, td=None):
        self.original_tagname_ = None
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.title = _cast(None, title)
        self.align = _cast(None, align)
        self.id = _cast(None, id)
        self.char = _cast(None, char)
        self.valign = _cast(None, valign)
        self.charoff = _cast(None, charoff)
        self.class_ = _cast(None, class_)
        self.dir = _cast(None, dir)
        if th is None:
            self.th = []
        else:
            self.th = th
        if td is None:
            self.td = []
        else:
            self.td = td
    def factory(*args_, **kwargs_):
        if tr.subclass:
            return tr.subclass(*args_, **kwargs_)
        else:
            return tr(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_th(self): return self.th
    def set_th(self, th): self.th = th
    def add_th(self, value): self.th.append(value)
    def insert_th(self, index, value): self.th[index] = value
    def get_td(self): return self.td
    def set_td(self, td): self.td = td
    def add_td(self, value): self.td.append(value)
    def insert_td(self, index, value): self.td[index] = value
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_align(self): return self.align
    def set_align(self, align): self.align = align
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_char(self): return self.char
    def set_char(self, char): self.char = char
    def get_valign(self): return self.valign
    def set_valign(self, valign): self.valign = valign
    def get_charoff(self): return self.charoff
    def set_charoff(self, charoff): self.charoff = charoff
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_Character(self, value):
        # Validate type Character, a restriction on xs:string.
        pass
    def validate_Length(self, value):
        # Validate type Length, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.th or
            self.td
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='tr', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='tr')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='tr', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='tr'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.align is not None and 'align' not in already_processed:
            already_processed.add('align')
            outfile.write(' align=%s' % (self.gds_format_string(quote_attrib(self.align).encode(ExternalEncoding), input_name='align'), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.char is not None and 'char' not in already_processed:
            already_processed.add('char')
            outfile.write(' char=%s' % (quote_attrib(self.char), ))
        if self.valign is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            outfile.write(' valign=%s' % (self.gds_format_string(quote_attrib(self.valign).encode(ExternalEncoding), input_name='valign'), ))
        if self.charoff is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            outfile.write(' charoff=%s' % (quote_attrib(self.charoff), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='tr', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for th_ in self.th:
            th_.export(outfile, level, namespace_, name_='th', pretty_print=pretty_print)
        for td_ in self.td:
            td_.export(outfile, level, namespace_, name_='td', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='tr', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://hl7.org/fhir}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://hl7.org/fhir}' + name_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.title is not None:
            element.set('title', self.title)
        if self.align is not None:
            element.set('align', self.gds_format_string(self.align))
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.char is not None:
            element.set('char', self.char)
        if self.valign is not None:
            element.set('valign', self.gds_format_string(self.valign))
        if self.charoff is not None:
            element.set('charoff', self.charoff)
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        for th_ in self.th:
            th_.to_etree(element, name_='th', mapping_=mapping_)
        for td_ in self.td:
            td_.to_etree(element, name_='td', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('align', node)
        if value is not None and 'align' not in already_processed:
            already_processed.add('align')
            self.align = value
            self.align = ' '.join(self.align.split())
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('char', node)
        if value is not None and 'char' not in already_processed:
            already_processed.add('char')
            self.char = value
            self.validate_Character(self.char)    # validate type Character
        value = find_attr_value_('valign', node)
        if value is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            self.valign = value
            self.valign = ' '.join(self.valign.split())
        value = find_attr_value_('charoff', node)
        if value is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            self.charoff = value
            self.validate_Length(self.charoff)    # validate type Length
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'th':
            obj_ = th.factory()
            obj_.build(child_)
            self.th.append(obj_)
            obj_.original_tagname_ = 'th'
        elif nodeName_ == 'td':
            obj_ = td.factory()
            obj_.build(child_)
            self.td.append(obj_)
            obj_.original_tagname_ = 'td'
# end class tr


class th(Flow):
    subclass = None
    superclass = Flow
    def __init__(self, p=None, h1=None, h2=None, h3=None, h4=None, h5=None, h6=None, div=None, ul=None, ol=None, dl=None, pre=None, hr=None, blockquote=None, table=None, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, rowspan='1', title=None, colspan='1', align=None, class_=None, char=None, headers=None, abbr_attr=None, valign=None, scope=None, charoff=None, id=None, dir=None, axis=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(th, self).__init__(p, h1, h2, h3, h4, h5, h6, div, ul, ol, dl, pre, hr, blockquote, table, a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.rowspan = _cast(None, rowspan)
        self.title = _cast(None, title)
        self.colspan = _cast(None, colspan)
        self.align = _cast(None, align)
        self.class_ = _cast(None, class_)
        self.char = _cast(None, char)
        self.headers = _cast(None, headers)
        self.abbr_attr = _cast(None, abbr_attr)
        self.valign = _cast(None, valign)
        self.scope = _cast(None, scope)
        self.charoff = _cast(None, charoff)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
        self.axis = _cast(None, axis)
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
        if th.subclass:
            return th.subclass(*args_, **kwargs_)
        else:
            return th(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_rowspan(self): return self.rowspan
    def set_rowspan(self, rowspan): self.rowspan = rowspan
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_colspan(self): return self.colspan
    def set_colspan(self, colspan): self.colspan = colspan
    def get_align(self): return self.align
    def set_align(self, align): self.align = align
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_char(self): return self.char
    def set_char(self, char): self.char = char
    def get_headers(self): return self.headers
    def set_headers(self, headers): self.headers = headers
    def get_abbr_attr(self): return self.abbr_attr
    def set_abbr_attr(self, abbr_attr): self.abbr_attr = abbr_attr
    def get_valign(self): return self.valign
    def set_valign(self, valign): self.valign = valign
    def get_scope(self): return self.scope
    def set_scope(self, scope): self.scope = scope
    def get_charoff(self): return self.charoff
    def set_charoff(self, charoff): self.charoff = charoff
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_axis(self): return self.axis
    def set_axis(self, axis): self.axis = axis
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Number(self, value):
        # Validate type Number, a restriction on xs:nonNegativeInteger.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_Character(self, value):
        # Validate type Character, a restriction on xs:string.
        pass
    def validate_Scope(self, value):
        # Validate type Scope, a restriction on xs:token.
        pass
    def validate_Length(self, value):
        # Validate type Length, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(th, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='th', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='th')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='th', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='th'):
        super(th, self).exportAttributes(outfile, level, already_processed, namespace_, name_='th')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.rowspan is not None and 'rowspan' not in already_processed:
            already_processed.add('rowspan')
            outfile.write(' rowspan=%s' % (quote_attrib(self.rowspan), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.colspan is not None and 'colspan' not in already_processed:
            already_processed.add('colspan')
            outfile.write(' colspan=%s' % (quote_attrib(self.colspan), ))
        if self.align is not None and 'align' not in already_processed:
            already_processed.add('align')
            outfile.write(' align=%s' % (self.gds_format_string(quote_attrib(self.align).encode(ExternalEncoding), input_name='align'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.char is not None and 'char' not in already_processed:
            already_processed.add('char')
            outfile.write(' char=%s' % (quote_attrib(self.char), ))
        if self.headers is not None and 'headers' not in already_processed:
            already_processed.add('headers')
            outfile.write(' headers=%s' % (self.gds_format_string(quote_attrib(self.headers).encode(ExternalEncoding), input_name='headers'), ))
        if self.abbr_attr is not None and 'abbr_attr' not in already_processed:
            already_processed.add('abbr_attr')
            outfile.write(' abbr=%s' % (self.gds_format_string(quote_attrib(self.abbr_attr).encode(ExternalEncoding), input_name='abbr_attr'), ))
        if self.valign is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            outfile.write(' valign=%s' % (self.gds_format_string(quote_attrib(self.valign).encode(ExternalEncoding), input_name='valign'), ))
        if self.scope is not None and 'scope' not in already_processed:
            already_processed.add('scope')
            outfile.write(' scope=%s' % (quote_attrib(self.scope), ))
        if self.charoff is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            outfile.write(' charoff=%s' % (quote_attrib(self.charoff), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
        if self.axis is not None and 'axis' not in already_processed:
            already_processed.add('axis')
            outfile.write(' axis=%s' % (self.gds_format_string(quote_attrib(self.axis).encode(ExternalEncoding), input_name='axis'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='th', fromsubclass_=False, pretty_print=True):
        super(th, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='th', mapping_=None):
        element = super(th, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.rowspan is not None:
            element.set('rowspan', self.rowspan)
        if self.title is not None:
            element.set('title', self.title)
        if self.colspan is not None:
            element.set('colspan', self.colspan)
        if self.align is not None:
            element.set('align', self.gds_format_string(self.align))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.char is not None:
            element.set('char', self.char)
        if self.headers is not None:
            element.set('headers', self.gds_format_string(self.headers))
        if self.abbr_attr is not None:
            element.set('abbr_attr', self.gds_format_string(self.abbr_attr))
        if self.valign is not None:
            element.set('valign', self.gds_format_string(self.valign))
        if self.scope is not None:
            element.set('scope', self.scope)
        if self.charoff is not None:
            element.set('charoff', self.charoff)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if self.axis is not None:
            element.set('axis', self.gds_format_string(self.axis))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('rowspan', node)
        if value is not None and 'rowspan' not in already_processed:
            already_processed.add('rowspan')
            try:
                self.rowspan = int(value)
            except ValueError as exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
            if self.rowspan < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
            self.validate_Number(self.rowspan)    # validate type Number
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('colspan', node)
        if value is not None and 'colspan' not in already_processed:
            already_processed.add('colspan')
            try:
                self.colspan = int(value)
            except ValueError as exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
            if self.colspan < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
            self.validate_Number(self.colspan)    # validate type Number
        value = find_attr_value_('align', node)
        if value is not None and 'align' not in already_processed:
            already_processed.add('align')
            self.align = value
            self.align = ' '.join(self.align.split())
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('char', node)
        if value is not None and 'char' not in already_processed:
            already_processed.add('char')
            self.char = value
            self.validate_Character(self.char)    # validate type Character
        value = find_attr_value_('headers', node)
        if value is not None and 'headers' not in already_processed:
            already_processed.add('headers')
            self.headers = value
        value = find_attr_value_('abbr', node)
        if value is not None and 'abbr_attr' not in already_processed:
            already_processed.add('abbr_attr')
            self.abbr_attr = value
        value = find_attr_value_('valign', node)
        if value is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            self.valign = value
            self.valign = ' '.join(self.valign.split())
        value = find_attr_value_('scope', node)
        if value is not None and 'scope' not in already_processed:
            already_processed.add('scope')
            self.scope = value
            self.scope = ' '.join(self.scope.split())
            self.validate_Scope(self.scope)    # validate type Scope
        value = find_attr_value_('charoff', node)
        if value is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            self.charoff = value
            self.validate_Length(self.charoff)    # validate type Length
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        value = find_attr_value_('axis', node)
        if value is not None and 'axis' not in already_processed:
            already_processed.add('axis')
            self.axis = value
        super(th, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(th, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class th


class td(Flow):
    subclass = None
    superclass = Flow
    def __init__(self, p=None, h1=None, h2=None, h3=None, h4=None, h5=None, h6=None, div=None, ul=None, ol=None, dl=None, pre=None, hr=None, blockquote=None, table=None, a=None, br=None, span=None, bdo=None, map=None, img=None, tt=None, i=None, b=None, big=None, small=None, em=None, strong=None, dfn=None, code=None, q=None, samp=None, kbd=None, var=None, cite=None, abbr=None, acronym=None, sub=None, sup=None, lang=None, style=None, rowspan='1', title=None, colspan='1', align=None, class_=None, char=None, headers=None, abbr_attr=None, valign=None, scope=None, charoff=None, id=None, dir=None, axis=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        super(td, self).__init__(p, h1, h2, h3, h4, h5, h6, div, ul, ol, dl, pre, hr, blockquote, table, a, br, span, bdo, map, img, tt, i, b, big, small, em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym, sub, sup, valueOf_, mixedclass_, content_, )
        self.lang = _cast(None, lang)
        self.style = _cast(None, style)
        self.rowspan = _cast(None, rowspan)
        self.title = _cast(None, title)
        self.colspan = _cast(None, colspan)
        self.align = _cast(None, align)
        self.class_ = _cast(None, class_)
        self.char = _cast(None, char)
        self.headers = _cast(None, headers)
        self.abbr_attr = _cast(None, abbr_attr)
        self.valign = _cast(None, valign)
        self.scope = _cast(None, scope)
        self.charoff = _cast(None, charoff)
        self.id = _cast(None, id)
        self.dir = _cast(None, dir)
        self.axis = _cast(None, axis)
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
        if td.subclass:
            return td.subclass(*args_, **kwargs_)
        else:
            return td(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lang(self): return self.lang
    def set_lang(self, lang): self.lang = lang
    def get_style(self): return self.style
    def set_style(self, style): self.style = style
    def get_rowspan(self): return self.rowspan
    def set_rowspan(self, rowspan): self.rowspan = rowspan
    def get_title(self): return self.title
    def set_title(self, title): self.title = title
    def get_colspan(self): return self.colspan
    def set_colspan(self, colspan): self.colspan = colspan
    def get_align(self): return self.align
    def set_align(self, align): self.align = align
    def get_class(self): return self.class_
    def set_class(self, class_): self.class_ = class_
    def get_char(self): return self.char
    def set_char(self, char): self.char = char
    def get_headers(self): return self.headers
    def set_headers(self, headers): self.headers = headers
    def get_abbr_attr(self): return self.abbr_attr
    def set_abbr_attr(self, abbr_attr): self.abbr_attr = abbr_attr
    def get_valign(self): return self.valign
    def set_valign(self, valign): self.valign = valign
    def get_scope(self): return self.scope
    def set_scope(self, scope): self.scope = scope
    def get_charoff(self): return self.charoff
    def set_charoff(self, charoff): self.charoff = charoff
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_dir(self): return self.dir
    def set_dir(self, dir): self.dir = dir
    def get_axis(self): return self.axis
    def set_axis(self, axis): self.axis = axis
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_StyleSheet(self, value):
        # Validate type StyleSheet, a restriction on xs:string.
        pass
    def validate_Number(self, value):
        # Validate type Number, a restriction on xs:nonNegativeInteger.
        pass
    def validate_Text(self, value):
        # Validate type Text, a restriction on xs:string.
        pass
    def validate_Character(self, value):
        # Validate type Character, a restriction on xs:string.
        pass
    def validate_Scope(self, value):
        # Validate type Scope, a restriction on xs:token.
        pass
    def validate_Length(self, value):
        # Validate type Length, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(td, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='td', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='td')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='td', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='td'):
        super(td, self).exportAttributes(outfile, level, already_processed, namespace_, name_='td')
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_format_string(quote_attrib(self.lang).encode(ExternalEncoding), input_name='lang'), ))
        if self.style is not None and 'style' not in already_processed:
            already_processed.add('style')
            outfile.write(' style=%s' % (quote_attrib(self.style), ))
        if self.rowspan is not None and 'rowspan' not in already_processed:
            already_processed.add('rowspan')
            outfile.write(' rowspan=%s' % (quote_attrib(self.rowspan), ))
        if self.title is not None and 'title' not in already_processed:
            already_processed.add('title')
            outfile.write(' title=%s' % (quote_attrib(self.title), ))
        if self.colspan is not None and 'colspan' not in already_processed:
            already_processed.add('colspan')
            outfile.write(' colspan=%s' % (quote_attrib(self.colspan), ))
        if self.align is not None and 'align' not in already_processed:
            already_processed.add('align')
            outfile.write(' align=%s' % (self.gds_format_string(quote_attrib(self.align).encode(ExternalEncoding), input_name='align'), ))
        if self.class_ is not None and 'class_' not in already_processed:
            already_processed.add('class_')
            outfile.write(' class=%s' % (quote_attrib(self.class_), ))
        if self.char is not None and 'char' not in already_processed:
            already_processed.add('char')
            outfile.write(' char=%s' % (quote_attrib(self.char), ))
        if self.headers is not None and 'headers' not in already_processed:
            already_processed.add('headers')
            outfile.write(' headers=%s' % (self.gds_format_string(quote_attrib(self.headers).encode(ExternalEncoding), input_name='headers'), ))
        if self.abbr_attr is not None and 'abbr_attr' not in already_processed:
            already_processed.add('abbr_attr')
            outfile.write(' abbr=%s' % (self.gds_format_string(quote_attrib(self.abbr_attr).encode(ExternalEncoding), input_name='abbr_attr'), ))
        if self.valign is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            outfile.write(' valign=%s' % (self.gds_format_string(quote_attrib(self.valign).encode(ExternalEncoding), input_name='valign'), ))
        if self.scope is not None and 'scope' not in already_processed:
            already_processed.add('scope')
            outfile.write(' scope=%s' % (quote_attrib(self.scope), ))
        if self.charoff is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            outfile.write(' charoff=%s' % (quote_attrib(self.charoff), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_format_string(quote_attrib(self.id).encode(ExternalEncoding), input_name='id'), ))
        if self.dir is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            outfile.write(' dir=%s' % (self.gds_format_string(quote_attrib(self.dir).encode(ExternalEncoding), input_name='dir'), ))
        if self.axis is not None and 'axis' not in already_processed:
            already_processed.add('axis')
            outfile.write(' axis=%s' % (self.gds_format_string(quote_attrib(self.axis).encode(ExternalEncoding), input_name='axis'), ))
    def exportChildren(self, outfile, level, namespace_='', name_='td', fromsubclass_=False, pretty_print=True):
        super(td, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='td', mapping_=None):
        element = super(td, self).to_etree(parent_element, name_, mapping_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.style is not None:
            element.set('style', self.style)
        if self.rowspan is not None:
            element.set('rowspan', self.rowspan)
        if self.title is not None:
            element.set('title', self.title)
        if self.colspan is not None:
            element.set('colspan', self.colspan)
        if self.align is not None:
            element.set('align', self.gds_format_string(self.align))
        if self.class_ is not None:
            element.set('class', self.class_)
        if self.char is not None:
            element.set('char', self.char)
        if self.headers is not None:
            element.set('headers', self.gds_format_string(self.headers))
        if self.abbr_attr is not None:
            element.set('abbr_attr', self.gds_format_string(self.abbr_attr))
        if self.valign is not None:
            element.set('valign', self.gds_format_string(self.valign))
        if self.scope is not None:
            element.set('scope', self.scope)
        if self.charoff is not None:
            element.set('charoff', self.charoff)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.dir is not None:
            element.set('dir', self.gds_format_string(self.dir))
        if self.axis is not None:
            element.set('axis', self.gds_format_string(self.axis))
        if mapping_ is not None:
            mapping_[self] = element
        return element
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
        value = find_attr_value_('style', node)
        if value is not None and 'style' not in already_processed:
            already_processed.add('style')
            self.style = value
            self.validate_StyleSheet(self.style)    # validate type StyleSheet
        value = find_attr_value_('rowspan', node)
        if value is not None and 'rowspan' not in already_processed:
            already_processed.add('rowspan')
            try:
                self.rowspan = int(value)
            except ValueError as exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
            if self.rowspan < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
            self.validate_Number(self.rowspan)    # validate type Number
        value = find_attr_value_('title', node)
        if value is not None and 'title' not in already_processed:
            already_processed.add('title')
            self.title = value
            self.validate_Text(self.title)    # validate type Text
        value = find_attr_value_('colspan', node)
        if value is not None and 'colspan' not in already_processed:
            already_processed.add('colspan')
            try:
                self.colspan = int(value)
            except ValueError as exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
            if self.colspan < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
            self.validate_Number(self.colspan)    # validate type Number
        value = find_attr_value_('align', node)
        if value is not None and 'align' not in already_processed:
            already_processed.add('align')
            self.align = value
            self.align = ' '.join(self.align.split())
        value = find_attr_value_('class', node)
        if value is not None and 'class' not in already_processed:
            already_processed.add('class')
            self.class_ = value
        value = find_attr_value_('char', node)
        if value is not None and 'char' not in already_processed:
            already_processed.add('char')
            self.char = value
            self.validate_Character(self.char)    # validate type Character
        value = find_attr_value_('headers', node)
        if value is not None and 'headers' not in already_processed:
            already_processed.add('headers')
            self.headers = value
        value = find_attr_value_('abbr', node)
        if value is not None and 'abbr_attr' not in already_processed:
            already_processed.add('abbr_attr')
            self.abbr_attr = value
        value = find_attr_value_('valign', node)
        if value is not None and 'valign' not in already_processed:
            already_processed.add('valign')
            self.valign = value
            self.valign = ' '.join(self.valign.split())
        value = find_attr_value_('scope', node)
        if value is not None and 'scope' not in already_processed:
            already_processed.add('scope')
            self.scope = value
            self.scope = ' '.join(self.scope.split())
            self.validate_Scope(self.scope)    # validate type Scope
        value = find_attr_value_('charoff', node)
        if value is not None and 'charoff' not in already_processed:
            already_processed.add('charoff')
            self.charoff = value
            self.validate_Length(self.charoff)    # validate type Length
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('dir', node)
        if value is not None and 'dir' not in already_processed:
            already_processed.add('dir')
            self.dir = value
            self.dir = ' '.join(self.dir.split())
        value = find_attr_value_('axis', node)
        if value is not None and 'axis' not in already_processed:
            already_processed.add('axis')
            self.axis = value
        super(td, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
        super(td, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class td
