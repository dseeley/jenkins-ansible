from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = """
        lookup: file_to_dict
        author: Dougal Seeley <ansible@dougalseeley.com>
        version_added: "0.9"
        short_description: read file contents as dict
        description:
            - This lookup returns a dictionary from a file on the Ansible controller's file system.
        options:
          _terms:
            description: path(s) of files to read
            required: True
        notes:
          - if read in variable context, the file can be interpreted as YAML if the content is valid to the parser.
          - this lookup does not understand globing --- use the fileglob lookup instead.
"""
from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.module_utils._text import to_text


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):

        ret = []
        for term in LookupBase._flatten(terms):
            self._display.v("File lookup term: %s" % term)

            # Find the file in the expected search path, using a class method that implements the 'expected' search path for Ansible plugins.
            lookupfile = self.find_file_in_search_path(variables, 'files', term)

            self._display.v(u"File lookup using %s as file" % lookupfile)
            if lookupfile:
                data_raw_bin, show_content = self._loader._get_file_contents(lookupfile)
                data_raw_text = to_text(data_raw_bin, errors='surrogate_or_strict')
                data_ansible_text = self._loader.load(data_raw_text, file_name=lookupfile, show_content=True)
                data_templated_text = self._templar.template(data_ansible_text, preserve_trailing_newlines=True, convert_data=True, escape_backslashes=False)

                ret.append(data_templated_text)
            else:
                raise AnsibleError("the file %s could not be found for the lookup" % term)

        return ret
