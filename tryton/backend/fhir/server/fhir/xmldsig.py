from .base_classes import *
from .support_functions import *

class RSAKeyValueType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Modulus=None, Exponent=None):
        self.original_tagname_ = None
        self.Modulus = Modulus
        self.validate_CryptoBinary(self.Modulus)
        self.Exponent = Exponent
        self.validate_CryptoBinary(self.Exponent)
    def factory(*args_, **kwargs_):
        if RSAKeyValueType.subclass:
            return RSAKeyValueType.subclass(*args_, **kwargs_)
        else:
            return RSAKeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Modulus(self): return self.Modulus
    def set_Modulus(self, Modulus): self.Modulus = Modulus
    def get_Exponent(self): return self.Exponent
    def set_Exponent(self, Exponent): self.Exponent = Exponent
    def validate_CryptoBinary(self, value):
        # Validate type CryptoBinary, a restriction on base64Binary.
        if value is not None and Validate_simpletypes_:
            pass
    def hasContent_(self):
        if (
            self.Modulus is not None or
            self.Exponent is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='RSAKeyValueType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RSAKeyValueType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='RSAKeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='RSAKeyValueType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='RSAKeyValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Modulus is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sModulus>%s</%sModulus>%s' % (namespace_, self.gds_format_base64(self.Modulus, input_name='Modulus'), namespace_, eol_))
        if self.Exponent is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sExponent>%s</%sExponent>%s' % (namespace_, self.gds_format_base64(self.Exponent, input_name='Exponent'), namespace_, eol_))
    def exportLiteral(self, outfile, level, name_='RSAKeyValueType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Modulus is not None:
            showIndent(outfile, level)
            outfile.write('Modulus=model_.xs_base64Binary(\n')
            self.Modulus.exportLiteral(outfile, level, name_='Modulus')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Exponent is not None:
            showIndent(outfile, level)
            outfile.write('Exponent=model_.xs_base64Binary(\n')
            self.Exponent.exportLiteral(outfile, level, name_='Exponent')
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Modulus':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Modulus')
            else:
                bval_ = None
            self.Modulus = bval_
            self.validate_CryptoBinary(self.Modulus)    # validate type CryptoBinary
        elif nodeName_ == 'Exponent':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Exponent')
            else:
                bval_ = None
            self.Exponent = bval_
            self.validate_CryptoBinary(self.Exponent)    # validate type CryptoBinary
# end class RSAKeyValueType

class DSAKeyValueType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, P=None, Q=None, G=None, Y=None, J=None, Seed=None, PgenCounter=None):
        self.original_tagname_ = None
        self.P = P
        self.validate_CryptoBinary(self.P)
        self.Q = Q
        self.validate_CryptoBinary(self.Q)
        self.G = G
        self.validate_CryptoBinary(self.G)
        self.Y = Y
        self.validate_CryptoBinary(self.Y)
        self.J = J
        self.validate_CryptoBinary(self.J)
        self.Seed = Seed
        self.validate_CryptoBinary(self.Seed)
        self.PgenCounter = PgenCounter
        self.validate_CryptoBinary(self.PgenCounter)
    def factory(*args_, **kwargs_):
        if DSAKeyValueType.subclass:
            return DSAKeyValueType.subclass(*args_, **kwargs_)
        else:
            return DSAKeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_P(self): return self.P
    def set_P(self, P): self.P = P
    def get_Q(self): return self.Q
    def set_Q(self, Q): self.Q = Q
    def get_G(self): return self.G
    def set_G(self, G): self.G = G
    def get_Y(self): return self.Y
    def set_Y(self, Y): self.Y = Y
    def get_J(self): return self.J
    def set_J(self, J): self.J = J
    def get_Seed(self): return self.Seed
    def set_Seed(self, Seed): self.Seed = Seed
    def get_PgenCounter(self): return self.PgenCounter
    def set_PgenCounter(self, PgenCounter): self.PgenCounter = PgenCounter
    def validate_CryptoBinary(self, value):
        # Validate type CryptoBinary, a restriction on base64Binary.
        if value is not None and Validate_simpletypes_:
            pass
    def hasContent_(self):
        if (
            self.P is not None or
            self.Q is not None or
            self.G is not None or
            self.Y is not None or
            self.J is not None or
            self.Seed is not None or
            self.PgenCounter is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DSAKeyValueType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DSAKeyValueType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DSAKeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DSAKeyValueType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='DSAKeyValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.P is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sP>%s</%sP>%s' % (namespace_, self.gds_format_base64(self.P, input_name='P'), namespace_, eol_))
        if self.Q is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sQ>%s</%sQ>%s' % (namespace_, self.gds_format_base64(self.Q, input_name='Q'), namespace_, eol_))
        if self.G is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sG>%s</%sG>%s' % (namespace_, self.gds_format_base64(self.G, input_name='G'), namespace_, eol_))
        if self.Y is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sY>%s</%sY>%s' % (namespace_, self.gds_format_base64(self.Y, input_name='Y'), namespace_, eol_))
        if self.J is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sJ>%s</%sJ>%s' % (namespace_, self.gds_format_base64(self.J, input_name='J'), namespace_, eol_))
        if self.Seed is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSeed>%s</%sSeed>%s' % (namespace_, self.gds_format_base64(self.Seed, input_name='Seed'), namespace_, eol_))
        if self.PgenCounter is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPgenCounter>%s</%sPgenCounter>%s' % (namespace_, self.gds_format_base64(self.PgenCounter, input_name='PgenCounter'), namespace_, eol_))
    def exportLiteral(self, outfile, level, name_='DSAKeyValueType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.P is not None:
            showIndent(outfile, level)
            outfile.write('P=model_.xs_base64Binary(\n')
            self.P.exportLiteral(outfile, level, name_='P')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Q is not None:
            showIndent(outfile, level)
            outfile.write('Q=model_.xs_base64Binary(\n')
            self.Q.exportLiteral(outfile, level, name_='Q')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.G is not None:
            showIndent(outfile, level)
            outfile.write('G=model_.xs_base64Binary(\n')
            self.G.exportLiteral(outfile, level, name_='G')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Y is not None:
            showIndent(outfile, level)
            outfile.write('Y=model_.xs_base64Binary(\n')
            self.Y.exportLiteral(outfile, level, name_='Y')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.J is not None:
            showIndent(outfile, level)
            outfile.write('J=model_.xs_base64Binary(\n')
            self.J.exportLiteral(outfile, level, name_='J')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Seed is not None:
            showIndent(outfile, level)
            outfile.write('Seed=model_.xs_base64Binary(\n')
            self.Seed.exportLiteral(outfile, level, name_='Seed')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.PgenCounter is not None:
            showIndent(outfile, level)
            outfile.write('PgenCounter=model_.xs_base64Binary(\n')
            self.PgenCounter.exportLiteral(outfile, level, name_='PgenCounter')
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'P':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'P')
            else:
                bval_ = None
            self.P = bval_
            self.validate_CryptoBinary(self.P)    # validate type CryptoBinary
        elif nodeName_ == 'Q':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Q')
            else:
                bval_ = None
            self.Q = bval_
            self.validate_CryptoBinary(self.Q)    # validate type CryptoBinary
        elif nodeName_ == 'G':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'G')
            else:
                bval_ = None
            self.G = bval_
            self.validate_CryptoBinary(self.G)    # validate type CryptoBinary
        elif nodeName_ == 'Y':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Y')
            else:
                bval_ = None
            self.Y = bval_
            self.validate_CryptoBinary(self.Y)    # validate type CryptoBinary
        elif nodeName_ == 'J':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'J')
            else:
                bval_ = None
            self.J = bval_
            self.validate_CryptoBinary(self.J)    # validate type CryptoBinary
        elif nodeName_ == 'Seed':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Seed')
            else:
                bval_ = None
            self.Seed = bval_
            self.validate_CryptoBinary(self.Seed)    # validate type CryptoBinary
        elif nodeName_ == 'PgenCounter':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'PgenCounter')
            else:
                bval_ = None
            self.PgenCounter = bval_
            self.validate_CryptoBinary(self.PgenCounter)    # validate type CryptoBinary
# end class DSAKeyValueType

class SignaturePropertyType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Target=None, Id=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        self.Target = _cast(None, Target)
        self.Id = _cast(None, Id)
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
        if SignaturePropertyType.subclass:
            return SignaturePropertyType.subclass(*args_, **kwargs_)
        else:
            return SignaturePropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_Target(self): return self.Target
    def set_Target(self, Target): self.Target = Target
    def get_Id(self): return self.Id
    def set_Id(self, Id): self.Id = Id
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
    def export(self, outfile, level, namespace_='', name_='SignaturePropertyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SignaturePropertyType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SignaturePropertyType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SignaturePropertyType'):
        if self.Target is not None and 'Target' not in already_processed:
            already_processed.add('Target')
            outfile.write(' Target=%s' % (quote_attrib(self.Target), ))
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SignaturePropertyType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='SignaturePropertyType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Target is not None and 'Target' not in already_processed:
            already_processed.add('Target')
            showIndent(outfile, level)
            outfile.write('Target=%s,\n' % (self.Target,))
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            showIndent(outfile, level)
            outfile.write('Id=%s,\n' % (self.Id,))
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
        value = find_attr_value_('Target', node)
        if value is not None and 'Target' not in already_processed:
            already_processed.add('Target')
            self.Target = value
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
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
# end class SignaturePropertyType

class SignaturePropertiesType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Id=None, SignatureProperty=None):
        self.original_tagname_ = None
        self.Id = _cast(None, Id)
        if SignatureProperty is None:
            self.SignatureProperty = []
        else:
            self.SignatureProperty = SignatureProperty
    def factory(*args_, **kwargs_):
        if SignaturePropertiesType.subclass:
            return SignaturePropertiesType.subclass(*args_, **kwargs_)
        else:
            return SignaturePropertiesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_SignatureProperty(self): return self.SignatureProperty
    def set_SignatureProperty(self, SignatureProperty): self.SignatureProperty = SignatureProperty
    def add_SignatureProperty(self, value): self.SignatureProperty.append(value)
    def insert_SignatureProperty_at(self, index, value): self.SignatureProperty.insert(index, value)
    def replace_SignatureProperty_at(self, index, value): self.SignatureProperty[index] = value
    def get_Id(self): return self.Id
    def set_Id(self, Id): self.Id = Id
    def hasContent_(self):
        if (
            self.SignatureProperty
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SignaturePropertiesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SignaturePropertiesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SignaturePropertiesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SignaturePropertiesType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SignaturePropertiesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SignatureProperty_ in self.SignatureProperty:
            SignatureProperty_.export(outfile, level, namespace_='ds:', name_='SignatureProperty', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='SignaturePropertiesType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            showIndent(outfile, level)
            outfile.write('Id=%s,\n' % (self.Id,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('SignatureProperty=[\n')
        level += 1
        for SignatureProperty_ in self.SignatureProperty:
            showIndent(outfile, level)
            outfile.write('model_.SignatureProperty(\n')
            SignatureProperty_.exportLiteral(outfile, level)
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'SignatureProperty':
            obj_ = SignaturePropertyType.factory()
            obj_.build(child_)
            self.SignatureProperty.append(obj_)
            obj_.original_tagname_ = 'SignatureProperty'
# end class SignaturePropertiesType

class ManifestType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Id=None, Reference=None):
        self.original_tagname_ = None
        self.Id = _cast(None, Id)
        if Reference is None:
            self.Reference = []
        else:
            self.Reference = Reference
    def factory(*args_, **kwargs_):
        if ManifestType.subclass:
            return ManifestType.subclass(*args_, **kwargs_)
        else:
            return ManifestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Reference(self): return self.Reference
    def set_Reference(self, Reference): self.Reference = Reference
    def add_Reference(self, value): self.Reference.append(value)
    def insert_Reference_at(self, index, value): self.Reference.insert(index, value)
    def replace_Reference_at(self, index, value): self.Reference[index] = value
    def get_Id(self): return self.Id
    def set_Id(self, Id): self.Id = Id
    def hasContent_(self):
        if (
            self.Reference
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ManifestType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ManifestType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ManifestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ManifestType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ManifestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Reference_ in self.Reference:
            Reference_.export(outfile, level, namespace_='ds:', name_='Reference', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ManifestType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            showIndent(outfile, level)
            outfile.write('Id=%s,\n' % (self.Id,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Reference=[\n')
        level += 1
        for Reference_ in self.Reference:
            showIndent(outfile, level)
            outfile.write('model_.Reference(\n')
            Reference_.exportLiteral(outfile, level)
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Reference':
            obj_ = ReferenceType.factory()
            obj_.build(child_)
            self.Reference.append(obj_)
            obj_.original_tagname_ = 'Reference'
# end class ManifestType

class ObjectType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, MimeType=None, Id=None, Encoding=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        self.MimeType = _cast(None, MimeType)
        self.Id = _cast(None, Id)
        self.Encoding = _cast(None, Encoding)
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
        if ObjectType.subclass:
            return ObjectType.subclass(*args_, **kwargs_)
        else:
            return ObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_MimeType(self): return self.MimeType
    def set_MimeType(self, MimeType): self.MimeType = MimeType
    def get_Id(self): return self.Id
    def set_Id(self, Id): self.Id = Id
    def get_Encoding(self): return self.Encoding
    def set_Encoding(self, Encoding): self.Encoding = Encoding
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
    def export(self, outfile, level, namespace_='', name_='ObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ObjectType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ObjectType'):
        if self.MimeType is not None and 'MimeType' not in already_processed:
            already_processed.add('MimeType')
            outfile.write(' MimeType=%s' % (quote_attrib(self.MimeType), ))
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
        if self.Encoding is not None and 'Encoding' not in already_processed:
            already_processed.add('Encoding')
            outfile.write(' Encoding=%s' % (quote_attrib(self.Encoding), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ObjectType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ObjectType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.MimeType is not None and 'MimeType' not in already_processed:
            already_processed.add('MimeType')
            showIndent(outfile, level)
            outfile.write('MimeType=%s,\n' % (self.MimeType,))
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            showIndent(outfile, level)
            outfile.write('Id=%s,\n' % (self.Id,))
        if self.Encoding is not None and 'Encoding' not in already_processed:
            already_processed.add('Encoding')
            showIndent(outfile, level)
            outfile.write('Encoding=%s,\n' % (self.Encoding,))
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
        value = find_attr_value_('MimeType', node)
        if value is not None and 'MimeType' not in already_processed:
            already_processed.add('MimeType')
            self.MimeType = value
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        value = find_attr_value_('Encoding', node)
        if value is not None and 'Encoding' not in already_processed:
            already_processed.add('Encoding')
            self.Encoding = value
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
# end class ObjectType

class SPKIDataType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, SPKISexp=None, anytypeobjs_=None):
        self.original_tagname_ = None
        if SPKISexp is None:
            self.SPKISexp = []
        else:
            self.SPKISexp = SPKISexp
        self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if SPKIDataType.subclass:
            return SPKIDataType.subclass(*args_, **kwargs_)
        else:
            return SPKIDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_SPKISexp(self): return self.SPKISexp
    def set_SPKISexp(self, SPKISexp): self.SPKISexp = SPKISexp
    def add_SPKISexp(self, value): self.SPKISexp.append(value)
    def insert_SPKISexp_at(self, index, value): self.SPKISexp.insert(index, value)
    def replace_SPKISexp_at(self, index, value): self.SPKISexp[index] = value
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def hasContent_(self):
        if (
            self.SPKISexp or
            self.anytypeobjs_ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SPKIDataType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SPKIDataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SPKIDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SPKIDataType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='SPKIDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SPKISexp_ in self.SPKISexp:
            SPKISexp_.export(outfile, level, namespace_, name_='SPKISexp', pretty_print=pretty_print)
        if self.anytypeobjs_ is not None:
            self.anytypeobjs_.export(outfile, level, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='SPKIDataType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('SPKISexp=[\n')
        level += 1
        for SPKISexp_ in self.SPKISexp:
            showIndent(outfile, level)
            outfile.write('model_.base64Binary(\n')
            SPKISexp_.exportLiteral(outfile, level, name_='base64Binary')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.anytypeobjs_ is not None:
            showIndent(outfile, level)
            outfile.write('anytypeobjs_=model_.anytypeobjs_(\n')
            self.anytypeobjs_.exportLiteral(outfile, level)
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'SPKISexp':
            class_obj_ = self.get_class_obj_(child_, base64Binary)
            obj_ = class_obj_.factory()
            obj_.build(child_)
            self.SPKISexp.append(obj_)
            obj_.original_tagname_ = 'SPKISexp'
        else:
            obj_ = self.gds_build_any(child_, 'SPKIDataType')
            if obj_ is not None:
                self.set_anytypeobjs_(obj_)
# end class SPKIDataType

class PGPDataType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, PGPKeyID=None, PGPKeyPacket=None, anytypeobjs_=None):
        self.original_tagname_ = None
        self.PGPKeyID = PGPKeyID
        self.PGPKeyPacket = PGPKeyPacket
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
        self.PGPKeyPacket = PGPKeyPacket
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if PGPDataType.subclass:
            return PGPDataType.subclass(*args_, **kwargs_)
        else:
            return PGPDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_PGPKeyID(self): return self.PGPKeyID
    def set_PGPKeyID(self, PGPKeyID): self.PGPKeyID = PGPKeyID
    def get_PGPKeyPacket(self): return self.PGPKeyPacket
    def set_PGPKeyPacket(self, PGPKeyPacket): self.PGPKeyPacket = PGPKeyPacket
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def get_PGPKeyPacket(self): return self.PGPKeyPacket
    def set_PGPKeyPacket(self, PGPKeyPacket): self.PGPKeyPacket = PGPKeyPacket
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def hasContent_(self):
        if (
            self.PGPKeyID is not None or
            self.PGPKeyPacket is not None or
            self.anytypeobjs_ or
            self.PGPKeyPacket is not None or
            self.anytypeobjs_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='PGPDataType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PGPDataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='PGPDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='PGPDataType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='PGPDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.PGPKeyID is not None:
            self.PGPKeyID.export(outfile, level, namespace_, name_='PGPKeyID', pretty_print=pretty_print)
        if self.PGPKeyPacket is not None:
            self.PGPKeyPacket.export(outfile, level, namespace_, name_='PGPKeyPacket', pretty_print=pretty_print)
        if self.PGPKeyPacket is not None:
            self.PGPKeyPacket.export(outfile, level, namespace_, name_='PGPKeyPacket', pretty_print=pretty_print)
        for obj_ in self.anytypeobjs_:
            obj_.export(outfile, level, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='PGPDataType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.PGPKeyID is not None:
            showIndent(outfile, level)
            outfile.write('PGPKeyID=model_.base64Binary(\n')
            self.PGPKeyID.exportLiteral(outfile, level, name_='PGPKeyID')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.PGPKeyPacket is not None:
            showIndent(outfile, level)
            outfile.write('PGPKeyPacket=model_.base64Binary(\n')
            self.PGPKeyPacket.exportLiteral(outfile, level, name_='PGPKeyPacket')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('anytypeobjs_=[\n')
        level += 1
        for anytypeobjs_ in self.anytypeobjs_:
            anytypeobjs_.exportLiteral(outfile, level)
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.PGPKeyPacket is not None:
            showIndent(outfile, level)
            outfile.write('PGPKeyPacket=model_.base64Binary(\n')
            self.PGPKeyPacket.exportLiteral(outfile, level, name_='PGPKeyPacket')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('anytypeobjs_=[\n')
        level += 1
        for anytypeobjs_ in self.anytypeobjs_:
            anytypeobjs_.exportLiteral(outfile, level)
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'PGPKeyID':
            class_obj_ = self.get_class_obj_(child_, base64Binary)
            obj_ = class_obj_.factory()
            obj_.build(child_)
            self.PGPKeyID = obj_
            obj_.original_tagname_ = 'PGPKeyID'
        elif nodeName_ == 'PGPKeyPacket':
            class_obj_ = self.get_class_obj_(child_, base64Binary)
            obj_ = class_obj_.factory()
            obj_.build(child_)
            self.PGPKeyPacket = obj_
            obj_.original_tagname_ = 'PGPKeyPacket'
        elif nodeName_ == 'PGPKeyPacket':
            class_obj_ = self.get_class_obj_(child_, base64Binary)
            obj_ = class_obj_.factory()
            obj_.build(child_)
            self.PGPKeyPacket = obj_
            obj_.original_tagname_ = 'PGPKeyPacket'
        else:
            obj_ = self.gds_build_any(child_, 'PGPDataType')
            if obj_ is not None:
                self.add_anytypeobjs_(obj_)
# end class PGPDataType

class KeyValueType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, DSAKeyValue=None, RSAKeyValue=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        self.DSAKeyValue = DSAKeyValue
        self.RSAKeyValue = RSAKeyValue
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
        if KeyValueType.subclass:
            return KeyValueType.subclass(*args_, **kwargs_)
        else:
            return KeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_DSAKeyValue(self): return self.DSAKeyValue
    def set_DSAKeyValue(self, DSAKeyValue): self.DSAKeyValue = DSAKeyValue
    def get_RSAKeyValue(self): return self.RSAKeyValue
    def set_RSAKeyValue(self, RSAKeyValue): self.RSAKeyValue = RSAKeyValue
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.DSAKeyValue is not None or
            self.RSAKeyValue is not None or
            self.anytypeobjs_ is not None or
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='KeyValueType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='KeyValueType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='KeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='KeyValueType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='KeyValueType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='KeyValueType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'DSAKeyValue':
            obj_ = DSAKeyValue.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'DSAKeyValue', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_DSAKeyValue'):
              self.add_DSAKeyValue(obj_.value)
            elif hasattr(self, 'set_DSAKeyValue'):
              self.set_DSAKeyValue(obj_.value)
        elif nodeName_ == 'RSAKeyValue':
            obj_ = RSAKeyValue.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'RSAKeyValue', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_RSAKeyValue'):
              self.add_RSAKeyValue(obj_.value)
            elif hasattr(self, 'set_RSAKeyValue'):
              self.set_RSAKeyValue(obj_.value)
        elif nodeName_ == '':
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
# end class KeyValueType

class RetrievalMethodType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Type=None, URI=None, Transforms=None):
        self.original_tagname_ = None
        self.Type = _cast(None, Type)
        self.URI = _cast(None, URI)
        self.Transforms = Transforms
    def factory(*args_, **kwargs_):
        if RetrievalMethodType.subclass:
            return RetrievalMethodType.subclass(*args_, **kwargs_)
        else:
            return RetrievalMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Transforms(self): return self.Transforms
    def set_Transforms(self, Transforms): self.Transforms = Transforms
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def get_URI(self): return self.URI
    def set_URI(self, URI): self.URI = URI
    def hasContent_(self):
        if (
            self.Transforms is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='RetrievalMethodType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RetrievalMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='RetrievalMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='RetrievalMethodType'):
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (quote_attrib(self.Type), ))
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            outfile.write(' URI=%s' % (quote_attrib(self.URI), ))
    def exportChildren(self, outfile, level, namespace_='', name_='RetrievalMethodType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transforms is not None:
            self.Transforms.export(outfile, level, namespace_='ds:', name_='Transforms', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='RetrievalMethodType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            showIndent(outfile, level)
            outfile.write('Type=%s,\n' % (self.Type,))
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            showIndent(outfile, level)
            outfile.write('URI=%s,\n' % (self.URI,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Transforms is not None:
            showIndent(outfile, level)
            outfile.write('Transforms=model_.Transforms(\n')
            self.Transforms.exportLiteral(outfile, level)
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
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
        value = find_attr_value_('URI', node)
        if value is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            self.URI = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Transforms':
            obj_ = TransformsType.factory()
            obj_.build(child_)
            self.Transforms = obj_
            obj_.original_tagname_ = 'Transforms'
# end class RetrievalMethodType

class X509DataType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, X509IssuerSerial=None, X509SKI=None, X509SubjectName=None, X509Certificate=None, X509CRL=None, anytypeobjs_=None):
        self.original_tagname_ = None
        if X509IssuerSerial is None:
            self.X509IssuerSerial = []
        else:
            self.X509IssuerSerial = X509IssuerSerial
        if X509SKI is None:
            self.X509SKI = []
        else:
            self.X509SKI = X509SKI
        if X509SubjectName is None:
            self.X509SubjectName = []
        else:
            self.X509SubjectName = X509SubjectName
        if X509Certificate is None:
            self.X509Certificate = []
        else:
            self.X509Certificate = X509Certificate
        if X509CRL is None:
            self.X509CRL = []
        else:
            self.X509CRL = X509CRL
        self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if X509DataType.subclass:
            return X509DataType.subclass(*args_, **kwargs_)
        else:
            return X509DataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_X509IssuerSerial(self): return self.X509IssuerSerial
    def set_X509IssuerSerial(self, X509IssuerSerial): self.X509IssuerSerial = X509IssuerSerial
    def add_X509IssuerSerial(self, value): self.X509IssuerSerial.append(value)
    def insert_X509IssuerSerial_at(self, index, value): self.X509IssuerSerial.insert(index, value)
    def replace_X509IssuerSerial_at(self, index, value): self.X509IssuerSerial[index] = value
    def get_X509SKI(self): return self.X509SKI
    def set_X509SKI(self, X509SKI): self.X509SKI = X509SKI
    def add_X509SKI(self, value): self.X509SKI.append(value)
    def insert_X509SKI_at(self, index, value): self.X509SKI.insert(index, value)
    def replace_X509SKI_at(self, index, value): self.X509SKI[index] = value
    def get_X509SubjectName(self): return self.X509SubjectName
    def set_X509SubjectName(self, X509SubjectName): self.X509SubjectName = X509SubjectName
    def add_X509SubjectName(self, value): self.X509SubjectName.append(value)
    def insert_X509SubjectName_at(self, index, value): self.X509SubjectName.insert(index, value)
    def replace_X509SubjectName_at(self, index, value): self.X509SubjectName[index] = value
    def get_X509Certificate(self): return self.X509Certificate
    def set_X509Certificate(self, X509Certificate): self.X509Certificate = X509Certificate
    def add_X509Certificate(self, value): self.X509Certificate.append(value)
    def insert_X509Certificate_at(self, index, value): self.X509Certificate.insert(index, value)
    def replace_X509Certificate_at(self, index, value): self.X509Certificate[index] = value
    def get_X509CRL(self): return self.X509CRL
    def set_X509CRL(self, X509CRL): self.X509CRL = X509CRL
    def add_X509CRL(self, value): self.X509CRL.append(value)
    def insert_X509CRL_at(self, index, value): self.X509CRL.insert(index, value)
    def replace_X509CRL_at(self, index, value): self.X509CRL[index] = value
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def hasContent_(self):
        if (
            self.X509IssuerSerial or
            self.X509SKI or
            self.X509SubjectName or
            self.X509Certificate or
            self.X509CRL or
            self.anytypeobjs_ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='X509DataType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='X509DataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='X509DataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='X509DataType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='X509DataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for X509IssuerSerial_ in self.X509IssuerSerial:
            X509IssuerSerial_.export(outfile, level, namespace_, name_='X509IssuerSerial', pretty_print=pretty_print)
        for X509SKI_ in self.X509SKI:
            X509SKI_.export(outfile, level, namespace_, name_='X509SKI', pretty_print=pretty_print)
        for X509SubjectName_ in self.X509SubjectName:
            X509SubjectName_.export(outfile, level, namespace_, name_='X509SubjectName', pretty_print=pretty_print)
        for X509Certificate_ in self.X509Certificate:
            X509Certificate_.export(outfile, level, namespace_, name_='X509Certificate', pretty_print=pretty_print)
        for X509CRL_ in self.X509CRL:
            X509CRL_.export(outfile, level, namespace_, name_='X509CRL', pretty_print=pretty_print)
        if self.anytypeobjs_ is not None:
            self.anytypeobjs_.export(outfile, level, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='X509DataType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('X509IssuerSerial=[\n')
        level += 1
        for X509IssuerSerial_ in self.X509IssuerSerial:
            showIndent(outfile, level)
            outfile.write('model_.X509IssuerSerialType(\n')
            X509IssuerSerial_.exportLiteral(outfile, level, name_='X509IssuerSerialType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('X509SKI=[\n')
        level += 1
        for X509SKI_ in self.X509SKI:
            showIndent(outfile, level)
            outfile.write('model_.base64Binary(\n')
            X509SKI_.exportLiteral(outfile, level, name_='base64Binary')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('X509SubjectName=[\n')
        level += 1
        for X509SubjectName_ in self.X509SubjectName:
            showIndent(outfile, level)
            outfile.write('model_.string(\n')
            X509SubjectName_.exportLiteral(outfile, level, name_='string')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('X509Certificate=[\n')
        level += 1
        for X509Certificate_ in self.X509Certificate:
            showIndent(outfile, level)
            outfile.write('model_.base64Binary(\n')
            X509Certificate_.exportLiteral(outfile, level, name_='base64Binary')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('X509CRL=[\n')
        level += 1
        for X509CRL_ in self.X509CRL:
            showIndent(outfile, level)
            outfile.write('model_.base64Binary(\n')
            X509CRL_.exportLiteral(outfile, level, name_='base64Binary')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.anytypeobjs_ is not None:
            showIndent(outfile, level)
            outfile.write('anytypeobjs_=model_.anytypeobjs_(\n')
            self.anytypeobjs_.exportLiteral(outfile, level)
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'X509IssuerSerial':
            obj_ = X509IssuerSerialType.factory()
            obj_.build(child_)
            self.X509IssuerSerial.append(obj_)
            obj_.original_tagname_ = 'X509IssuerSerial'
        elif nodeName_ == 'X509SKI':
            class_obj_ = self.get_class_obj_(child_, base64Binary)
            obj_ = class_obj_.factory()
            obj_.build(child_)
            self.X509SKI.append(obj_)
            obj_.original_tagname_ = 'X509SKI'
        elif nodeName_ == 'X509SubjectName':
            obj_ = string.factory()
            obj_.build(child_)
            self.X509SubjectName.append(obj_)
            obj_.original_tagname_ = 'X509SubjectName'
        elif nodeName_ == 'X509Certificate':
            class_obj_ = self.get_class_obj_(child_, base64Binary)
            obj_ = class_obj_.factory()
            obj_.build(child_)
            self.X509Certificate.append(obj_)
            obj_.original_tagname_ = 'X509Certificate'
        elif nodeName_ == 'X509CRL':
            class_obj_ = self.get_class_obj_(child_, base64Binary)
            obj_ = class_obj_.factory()
            obj_.build(child_)
            self.X509CRL.append(obj_)
            obj_.original_tagname_ = 'X509CRL'
        else:
            obj_ = self.gds_build_any(child_, 'X509DataType')
            if obj_ is not None:
                self.set_anytypeobjs_(obj_)
# end class X509DataType

class X509IssuerSerialType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, X509IssuerName=None, X509SerialNumber=None):
        self.original_tagname_ = None
        self.X509IssuerName = X509IssuerName
        self.X509SerialNumber = X509SerialNumber
    def factory(*args_, **kwargs_):
        if X509IssuerSerialType.subclass:
            return X509IssuerSerialType.subclass(*args_, **kwargs_)
        else:
            return X509IssuerSerialType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_X509IssuerName(self): return self.X509IssuerName
    def set_X509IssuerName(self, X509IssuerName): self.X509IssuerName = X509IssuerName
    def get_X509SerialNumber(self): return self.X509SerialNumber
    def set_X509SerialNumber(self, X509SerialNumber): self.X509SerialNumber = X509SerialNumber
    def hasContent_(self):
        if (
            self.X509IssuerName is not None or
            self.X509SerialNumber is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='X509IssuerSerialType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='X509IssuerSerialType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='X509IssuerSerialType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='X509IssuerSerialType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='X509IssuerSerialType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.X509IssuerName is not None:
            self.X509IssuerName.export(outfile, level, namespace_, name_='X509IssuerName', pretty_print=pretty_print)
        if self.X509SerialNumber is not None:
            self.X509SerialNumber.export(outfile, level, namespace_, name_='X509SerialNumber', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='X509IssuerSerialType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.X509IssuerName is not None:
            showIndent(outfile, level)
            outfile.write('X509IssuerName=model_.string(\n')
            self.X509IssuerName.exportLiteral(outfile, level, name_='X509IssuerName')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.X509SerialNumber is not None:
            showIndent(outfile, level)
            outfile.write('X509SerialNumber=model_.integer(\n')
            self.X509SerialNumber.exportLiteral(outfile, level, name_='X509SerialNumber')
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'X509IssuerName':
            obj_ = string.factory()
            obj_.build(child_)
            self.X509IssuerName = obj_
            obj_.original_tagname_ = 'X509IssuerName'
        elif nodeName_ == 'X509SerialNumber':
            obj_ = integer.factory()
            obj_.build(child_)
            self.X509SerialNumber = obj_
            obj_.original_tagname_ = 'X509SerialNumber'
# end class X509IssuerSerialType

class DigestMethodType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        self.Algorithm = _cast(None, Algorithm)
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
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
        if DigestMethodType.subclass:
            return DigestMethodType.subclass(*args_, **kwargs_)
        else:
            return DigestMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def get_Algorithm(self): return self.Algorithm
    def set_Algorithm(self, Algorithm): self.Algorithm = Algorithm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.anytypeobjs_ or
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='DigestMethodType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DigestMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='DigestMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DigestMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def exportChildren(self, outfile, level, namespace_='', name_='DigestMethodType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='DigestMethodType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            showIndent(outfile, level)
            outfile.write('Algorithm=%s,\n' % (self.Algorithm,))
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
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
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
# end class DigestMethodType

class KeyInfoType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Id=None, KeyName=None, KeyValue=None, RetrievalMethod=None, X509Data=None, PGPData=None, SPKIData=None, MgmtData=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        self.Id = _cast(None, Id)
        if KeyName is None:
            self.KeyName = []
        else:
            self.KeyName = KeyName
        if KeyValue is None:
            self.KeyValue = []
        else:
            self.KeyValue = KeyValue
        if RetrievalMethod is None:
            self.RetrievalMethod = []
        else:
            self.RetrievalMethod = RetrievalMethod
        if X509Data is None:
            self.X509Data = []
        else:
            self.X509Data = X509Data
        if PGPData is None:
            self.PGPData = []
        else:
            self.PGPData = PGPData
        if SPKIData is None:
            self.SPKIData = []
        else:
            self.SPKIData = SPKIData
        if MgmtData is None:
            self.MgmtData = []
        else:
            self.MgmtData = MgmtData
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
        if KeyInfoType.subclass:
            return KeyInfoType.subclass(*args_, **kwargs_)
        else:
            return KeyInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_KeyName(self): return self.KeyName
    def set_KeyName(self, KeyName): self.KeyName = KeyName
    def add_KeyName(self, value): self.KeyName.append(value)
    def insert_KeyName_at(self, index, value): self.KeyName.insert(index, value)
    def replace_KeyName_at(self, index, value): self.KeyName[index] = value
    def get_KeyValue(self): return self.KeyValue
    def set_KeyValue(self, KeyValue): self.KeyValue = KeyValue
    def add_KeyValue(self, value): self.KeyValue.append(value)
    def insert_KeyValue_at(self, index, value): self.KeyValue.insert(index, value)
    def replace_KeyValue_at(self, index, value): self.KeyValue[index] = value
    def get_RetrievalMethod(self): return self.RetrievalMethod
    def set_RetrievalMethod(self, RetrievalMethod): self.RetrievalMethod = RetrievalMethod
    def add_RetrievalMethod(self, value): self.RetrievalMethod.append(value)
    def insert_RetrievalMethod_at(self, index, value): self.RetrievalMethod.insert(index, value)
    def replace_RetrievalMethod_at(self, index, value): self.RetrievalMethod[index] = value
    def get_X509Data(self): return self.X509Data
    def set_X509Data(self, X509Data): self.X509Data = X509Data
    def add_X509Data(self, value): self.X509Data.append(value)
    def insert_X509Data_at(self, index, value): self.X509Data.insert(index, value)
    def replace_X509Data_at(self, index, value): self.X509Data[index] = value
    def get_PGPData(self): return self.PGPData
    def set_PGPData(self, PGPData): self.PGPData = PGPData
    def add_PGPData(self, value): self.PGPData.append(value)
    def insert_PGPData_at(self, index, value): self.PGPData.insert(index, value)
    def replace_PGPData_at(self, index, value): self.PGPData[index] = value
    def get_SPKIData(self): return self.SPKIData
    def set_SPKIData(self, SPKIData): self.SPKIData = SPKIData
    def add_SPKIData(self, value): self.SPKIData.append(value)
    def insert_SPKIData_at(self, index, value): self.SPKIData.insert(index, value)
    def replace_SPKIData_at(self, index, value): self.SPKIData[index] = value
    def get_MgmtData(self): return self.MgmtData
    def set_MgmtData(self, MgmtData): self.MgmtData = MgmtData
    def add_MgmtData(self, value): self.MgmtData.append(value)
    def insert_MgmtData_at(self, index, value): self.MgmtData.insert(index, value)
    def replace_MgmtData_at(self, index, value): self.MgmtData[index] = value
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_Id(self): return self.Id
    def set_Id(self, Id): self.Id = Id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.KeyName or
            self.KeyValue or
            self.RetrievalMethod or
            self.X509Data or
            self.PGPData or
            self.SPKIData or
            self.MgmtData or
            self.anytypeobjs_ is not None or
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='KeyInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='KeyInfoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='KeyInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='KeyInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='KeyInfoType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='KeyInfoType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            showIndent(outfile, level)
            outfile.write('Id=%s,\n' % (self.Id,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'KeyName':
            obj_ = KeyName.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'KeyName', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_KeyName'):
              self.add_KeyName(obj_.value)
            elif hasattr(self, 'set_KeyName'):
              self.set_KeyName(obj_.value)
        elif nodeName_ == 'KeyValue':
            obj_ = KeyValue.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'KeyValue', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_KeyValue'):
              self.add_KeyValue(obj_.value)
            elif hasattr(self, 'set_KeyValue'):
              self.set_KeyValue(obj_.value)
        elif nodeName_ == 'RetrievalMethod':
            obj_ = RetrievalMethod.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'RetrievalMethod', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_RetrievalMethod'):
              self.add_RetrievalMethod(obj_.value)
            elif hasattr(self, 'set_RetrievalMethod'):
              self.set_RetrievalMethod(obj_.value)
        elif nodeName_ == 'X509Data':
            obj_ = X509Data.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'X509Data', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_X509Data'):
              self.add_X509Data(obj_.value)
            elif hasattr(self, 'set_X509Data'):
              self.set_X509Data(obj_.value)
        elif nodeName_ == 'PGPData':
            obj_ = PGPData.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'PGPData', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_PGPData'):
              self.add_PGPData(obj_.value)
            elif hasattr(self, 'set_PGPData'):
              self.set_PGPData(obj_.value)
        elif nodeName_ == 'SPKIData':
            obj_ = SPKIData.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'SPKIData', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_SPKIData'):
              self.add_SPKIData(obj_.value)
            elif hasattr(self, 'set_SPKIData'):
              self.set_SPKIData(obj_.value)
        elif nodeName_ == 'MgmtData':
            obj_ = MgmtData.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'MgmtData', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_MgmtData'):
              self.add_MgmtData(obj_.value)
            elif hasattr(self, 'set_MgmtData'):
              self.set_MgmtData(obj_.value)
        elif nodeName_ == '':
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
# end class KeyInfoType

class TransformsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Transform=None):
        self.original_tagname_ = None
        if Transform is None:
            self.Transform = []
        else:
            self.Transform = Transform
    def factory(*args_, **kwargs_):
        if TransformsType.subclass:
            return TransformsType.subclass(*args_, **kwargs_)
        else:
            return TransformsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Transform(self): return self.Transform
    def set_Transform(self, Transform): self.Transform = Transform
    def add_Transform(self, value): self.Transform.append(value)
    def insert_Transform_at(self, index, value): self.Transform.insert(index, value)
    def replace_Transform_at(self, index, value): self.Transform[index] = value
    def hasContent_(self):
        if (
            self.Transform
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='TransformsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='TransformsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='TransformsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='TransformsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='TransformsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Transform_ in self.Transform:
            Transform_.export(outfile, level, namespace_='ds:', name_='Transform', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='TransformsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Transform=[\n')
        level += 1
        for Transform_ in self.Transform:
            showIndent(outfile, level)
            outfile.write('model_.Transform(\n')
            Transform_.exportLiteral(outfile, level)
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Transform':
            obj_ = TransformType.factory()
            obj_.build(child_)
            self.Transform.append(obj_)
            obj_.original_tagname_ = 'Transform'
# end class TransformsType

class TransformType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, anytypeobjs_=None, XPath=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.anytypeobjs_ = anytypeobjs_
        if XPath is None:
            self.XPath = []
        else:
            self.XPath = XPath
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
        if TransformType.subclass:
            return TransformType.subclass(*args_, **kwargs_)
        else:
            return TransformType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_XPath(self): return self.XPath
    def set_XPath(self, XPath): self.XPath = XPath
    def add_XPath(self, value): self.XPath.append(value)
    def insert_XPath_at(self, index, value): self.XPath.insert(index, value)
    def replace_XPath_at(self, index, value): self.XPath[index] = value
    def get_Algorithm(self): return self.Algorithm
    def set_Algorithm(self, Algorithm): self.Algorithm = Algorithm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.anytypeobjs_ is not None or
            self.XPath or
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='TransformType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='TransformType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='TransformType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='TransformType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def exportChildren(self, outfile, level, namespace_='', name_='TransformType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='TransformType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            showIndent(outfile, level)
            outfile.write('Algorithm=%s,\n' % (self.Algorithm,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
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
        elif nodeName_ == 'XPath':
            obj_ = string.factory()
            obj_.build(child_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'XPath', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_XPath'):
              self.add_XPath(obj_.value)
            elif hasattr(self, 'set_XPath'):
              self.set_XPath(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class TransformType

class CanonicalizationMethodType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        self.Algorithm = _cast(None, Algorithm)
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
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
        if CanonicalizationMethodType.subclass:
            return CanonicalizationMethodType.subclass(*args_, **kwargs_)
        else:
            return CanonicalizationMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def get_Algorithm(self): return self.Algorithm
    def set_Algorithm(self, Algorithm): self.Algorithm = Algorithm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.anytypeobjs_ or
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='CanonicalizationMethodType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CanonicalizationMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='CanonicalizationMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='CanonicalizationMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def exportChildren(self, outfile, level, namespace_='', name_='CanonicalizationMethodType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='CanonicalizationMethodType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            showIndent(outfile, level)
            outfile.write('Algorithm=%s,\n' % (self.Algorithm,))
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
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
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
# end class CanonicalizationMethodType

class SignatureMethodType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, HMACOutputLength=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        self.original_tagname_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.HMACOutputLength = HMACOutputLength
        self.validate_HMACOutputLengthType(self.HMACOutputLength)
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
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
        if SignatureMethodType.subclass:
            return SignatureMethodType.subclass(*args_, **kwargs_)
        else:
            return SignatureMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_HMACOutputLength(self): return self.HMACOutputLength
    def set_HMACOutputLength(self, HMACOutputLength): self.HMACOutputLength = HMACOutputLength
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def get_Algorithm(self): return self.Algorithm
    def set_Algorithm(self, Algorithm): self.Algorithm = Algorithm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_HMACOutputLengthType(self, value):
        # Validate type HMACOutputLengthType, a restriction on integer.
        if value is not None and Validate_simpletypes_:
            pass
    def hasContent_(self):
        if (
            self.HMACOutputLength is not None or
            self.anytypeobjs_ or
            self.valueOf_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SignatureMethodType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SignatureMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SignatureMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SignatureMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SignatureMethodType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespace_, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='SignatureMethodType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            showIndent(outfile, level)
            outfile.write('Algorithm=%s,\n' % (self.Algorithm,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
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
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'HMACOutputLength' and child_.text is not None:
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError) as exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeInteger, 'HMACOutputLength', ival_)
            self.content_.append(obj_)
        elif nodeName_ == '':
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
# end class SignatureMethodType

class ReferenceType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Type=None, Id=None, URI=None, Transforms=None, DigestMethod=None, DigestValue=None):
        self.original_tagname_ = None
        self.Type = _cast(None, Type)
        self.Id = _cast(None, Id)
        self.URI = _cast(None, URI)
        self.Transforms = Transforms
        self.DigestMethod = DigestMethod
        self.DigestValue = DigestValue
    def factory(*args_, **kwargs_):
        if ReferenceType.subclass:
            return ReferenceType.subclass(*args_, **kwargs_)
        else:
            return ReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Transforms(self): return self.Transforms
    def set_Transforms(self, Transforms): self.Transforms = Transforms
    def get_DigestMethod(self): return self.DigestMethod
    def set_DigestMethod(self, DigestMethod): self.DigestMethod = DigestMethod
    def get_DigestValue(self): return self.DigestValue
    def set_DigestValue(self, DigestValue): self.DigestValue = DigestValue
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def get_Id(self): return self.Id
    def set_Id(self, Id): self.Id = Id
    def get_URI(self): return self.URI
    def set_URI(self, URI): self.URI = URI
    def hasContent_(self):
        if (
            self.Transforms is not None or
            self.DigestMethod is not None or
            self.DigestValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='ReferenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ReferenceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='ReferenceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ReferenceType'):
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (quote_attrib(self.Type), ))
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            outfile.write(' URI=%s' % (quote_attrib(self.URI), ))
    def exportChildren(self, outfile, level, namespace_='', name_='ReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transforms is not None:
            self.Transforms.export(outfile, level, namespace_='ds:', name_='Transforms', pretty_print=pretty_print)
        if self.DigestMethod is not None:
            self.DigestMethod.export(outfile, level, namespace_='ds:', name_='DigestMethod', pretty_print=pretty_print)
        if self.DigestValue is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDigestValue>%s</%sDigestValue>%s' % (namespace_, self.gds_format_base64(self.DigestValue, input_name='DigestValue'), namespace_, eol_))
    def exportLiteral(self, outfile, level, name_='ReferenceType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            showIndent(outfile, level)
            outfile.write('Type=%s,\n' % (self.Type,))
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            showIndent(outfile, level)
            outfile.write('Id=%s,\n' % (self.Id,))
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            showIndent(outfile, level)
            outfile.write('URI=%s,\n' % (self.URI,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Transforms is not None:
            showIndent(outfile, level)
            outfile.write('Transforms=model_.Transforms(\n')
            self.Transforms.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.DigestMethod is not None:
            showIndent(outfile, level)
            outfile.write('DigestMethod=model_.DigestMethod(\n')
            self.DigestMethod.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.DigestValue is not None:
            showIndent(outfile, level)
            outfile.write('DigestValue=model_.xs_base64Binary(\n')
            self.DigestValue.exportLiteral(outfile, level, name_='DigestValue')
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
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        value = find_attr_value_('URI', node)
        if value is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            self.URI = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Transforms':
            obj_ = TransformsType.factory()
            obj_.build(child_)
            self.Transforms = obj_
            obj_.original_tagname_ = 'Transforms'
        elif nodeName_ == 'DigestMethod':
            obj_ = DigestMethodType.factory()
            obj_.build(child_)
            self.DigestMethod = obj_
            obj_.original_tagname_ = 'DigestMethod'
        elif nodeName_ == 'DigestValue':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'DigestValue')
            else:
                bval_ = None
            self.DigestValue = bval_
# end class ReferenceType

class SignatureType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Id=None, SignedInfo=None, SignatureValue=None, KeyInfo=None, Object=None):
        self.original_tagname_ = None
        self.Id = _cast(None, Id)
        self.SignedInfo = SignedInfo
        self.SignatureValue = SignatureValue
        self.KeyInfo = KeyInfo
        if Object is None:
            self.Object = []
        else:
            self.Object = Object
    def factory(*args_, **kwargs_):
        if SignatureType.subclass:
            return SignatureType.subclass(*args_, **kwargs_)
        else:
            return SignatureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_SignedInfo(self): return self.SignedInfo
    def set_SignedInfo(self, SignedInfo): self.SignedInfo = SignedInfo
    def get_SignatureValue(self): return self.SignatureValue
    def set_SignatureValue(self, SignatureValue): self.SignatureValue = SignatureValue
    def get_KeyInfo(self): return self.KeyInfo
    def set_KeyInfo(self, KeyInfo): self.KeyInfo = KeyInfo
    def get_Object(self): return self.Object
    def set_Object(self, Object): self.Object = Object
    def add_Object(self, value): self.Object.append(value)
    def insert_Object_at(self, index, value): self.Object.insert(index, value)
    def replace_Object_at(self, index, value): self.Object[index] = value
    def get_Id(self): return self.Id
    def set_Id(self, Id): self.Id = Id
    def hasContent_(self):
        if (
            self.SignedInfo is not None or
            self.SignatureValue is not None or
            self.KeyInfo is not None or
            self.Object
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SignatureType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SignatureType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SignatureType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SignatureType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SignatureType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SignedInfo is not None:
            self.SignedInfo.export(outfile, level, namespace_='ds:', name_='SignedInfo', pretty_print=pretty_print)
        if self.SignatureValue is not None:
            self.SignatureValue.export(outfile, level, namespace_='ds:', name_='SignatureValue', pretty_print=pretty_print)
        if self.KeyInfo is not None:
            self.KeyInfo.export(outfile, level, namespace_='ds:', name_='KeyInfo', pretty_print=pretty_print)
        for Object_ in self.Object:
            Object_.export(outfile, level, namespace_='ds:', name_='Object', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='SignatureType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            showIndent(outfile, level)
            outfile.write('Id=%s,\n' % (self.Id,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.SignedInfo is not None:
            showIndent(outfile, level)
            outfile.write('SignedInfo=model_.SignedInfo(\n')
            self.SignedInfo.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.SignatureValue is not None:
            showIndent(outfile, level)
            outfile.write('SignatureValue=model_.SignatureValue(\n')
            self.SignatureValue.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.KeyInfo is not None:
            showIndent(outfile, level)
            outfile.write('KeyInfo=model_.KeyInfo(\n')
            self.KeyInfo.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Object=[\n')
        level += 1
        for Object_ in self.Object:
            showIndent(outfile, level)
            outfile.write('model_.Object(\n')
            Object_.exportLiteral(outfile, level)
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'SignedInfo':
            obj_ = SignedInfoType.factory()
            obj_.build(child_)
            self.SignedInfo = obj_
            obj_.original_tagname_ = 'SignedInfo'
        elif nodeName_ == 'SignatureValue':
            obj_ = SignatureValueType.factory()
            obj_.build(child_)
            self.SignatureValue = obj_
            obj_.original_tagname_ = 'SignatureValue'
        elif nodeName_ == 'KeyInfo':
            obj_ = KeyInfoType.factory()
            obj_.build(child_)
            self.KeyInfo = obj_
            obj_.original_tagname_ = 'KeyInfo'
        elif nodeName_ == 'Object':
            obj_ = ObjectType.factory()
            obj_.build(child_)
            self.Object.append(obj_)
            obj_.original_tagname_ = 'Object'
# end class SignatureType

class SignatureValueType(base64Binary):
    subclass = None
    superclass = base64Binary
    def __init__(self, id=None, extension=None, value=None, Id=None, valueOf_=None):
        self.original_tagname_ = None
        super(SignatureValueType, self).__init__(id, extension, value, valueOf_, )
        self.Id = _cast(None, Id)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if SignatureValueType.subclass:
            return SignatureValueType.subclass(*args_, **kwargs_)
        else:
            return SignatureValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Id(self): return self.Id
    def set_Id(self, Id): self.Id = Id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(SignatureValueType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SignatureValueType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SignatureValueType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SignatureValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SignatureValueType'):
        super(SignatureValueType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SignatureValueType')
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SignatureValueType', fromsubclass_=False, pretty_print=True):
        super(SignatureValueType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='SignatureValueType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            showIndent(outfile, level)
            outfile.write('Id=%s,\n' % (self.Id,))
        super(SignatureValueType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(SignatureValueType, self).exportLiteralChildren(outfile, level, name_)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        super(SignatureValueType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class SignatureValueType

class SignedInfoType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Id=None, CanonicalizationMethod=None, SignatureMethod=None, Reference=None):
        self.original_tagname_ = None
        self.Id = _cast(None, Id)
        self.CanonicalizationMethod = CanonicalizationMethod
        self.SignatureMethod = SignatureMethod
        if Reference is None:
            self.Reference = []
        else:
            self.Reference = Reference
    def factory(*args_, **kwargs_):
        if SignedInfoType.subclass:
            return SignedInfoType.subclass(*args_, **kwargs_)
        else:
            return SignedInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_CanonicalizationMethod(self): return self.CanonicalizationMethod
    def set_CanonicalizationMethod(self, CanonicalizationMethod): self.CanonicalizationMethod = CanonicalizationMethod
    def get_SignatureMethod(self): return self.SignatureMethod
    def set_SignatureMethod(self, SignatureMethod): self.SignatureMethod = SignatureMethod
    def get_Reference(self): return self.Reference
    def set_Reference(self, Reference): self.Reference = Reference
    def add_Reference(self, value): self.Reference.append(value)
    def insert_Reference_at(self, index, value): self.Reference.insert(index, value)
    def replace_Reference_at(self, index, value): self.Reference[index] = value
    def get_Id(self): return self.Id
    def set_Id(self, Id): self.Id = Id
    def hasContent_(self):
        if (
            self.CanonicalizationMethod is not None or
            self.SignatureMethod is not None or
            self.Reference
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='SignedInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SignedInfoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='SignedInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SignedInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespace_='', name_='SignedInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CanonicalizationMethod is not None:
            self.CanonicalizationMethod.export(outfile, level, namespace_='ds:', name_='CanonicalizationMethod', pretty_print=pretty_print)
        if self.SignatureMethod is not None:
            self.SignatureMethod.export(outfile, level, namespace_='ds:', name_='SignatureMethod', pretty_print=pretty_print)
        for Reference_ in self.Reference:
            Reference_.export(outfile, level, namespace_='ds:', name_='Reference', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='SignedInfoType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            showIndent(outfile, level)
            outfile.write('Id=%s,\n' % (self.Id,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.CanonicalizationMethod is not None:
            showIndent(outfile, level)
            outfile.write('CanonicalizationMethod=model_.CanonicalizationMethod(\n')
            self.CanonicalizationMethod.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.SignatureMethod is not None:
            showIndent(outfile, level)
            outfile.write('SignatureMethod=model_.SignatureMethod(\n')
            self.SignatureMethod.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Reference=[\n')
        level += 1
        for Reference_ in self.Reference:
            showIndent(outfile, level)
            outfile.write('model_.Reference(\n')
            Reference_.exportLiteral(outfile, level)
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'CanonicalizationMethod':
            obj_ = CanonicalizationMethodType.factory()
            obj_.build(child_)
            self.CanonicalizationMethod = obj_
            obj_.original_tagname_ = 'CanonicalizationMethod'
        elif nodeName_ == 'SignatureMethod':
            obj_ = SignatureMethodType.factory()
            obj_.build(child_)
            self.SignatureMethod = obj_
            obj_.original_tagname_ = 'SignatureMethod'
        elif nodeName_ == 'Reference':
            obj_ = ReferenceType.factory()
            obj_.build(child_)
            self.Reference.append(obj_)
            obj_.original_tagname_ = 'Reference'
# end class SignedInfoType
