# mostly constants related to Creative Commons
# let's be DRY with these parameters

INFO_CC = (
    ('CC BY-NC-ND', 'by-nc-nd', 'Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported (CC BY-NC-ND 3.0)', 'http://creativecommons.org/licenses/by-nc-nd/3.0/'),     
    ('CC BY-NC-SA', 'by-nc-sa', 'Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)', 'http://creativecommons.org/licenses/by-nc-sa/3.0/'),
    ('CC BY-NC', 'by-nc', 'Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0)', 'http://creativecommons.org/licenses/by-nc/3.0/'),
    ('CC BY-ND', 'by-nd', 'Creative Commons Attribution-NoDerivs 3.0 Unported (CC BY-ND 3.0)', 'http://creativecommons.org/licenses/by-nd/3.0/'), 
    ('CC BY-SA', 'by-sa', 'Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)', 'http://creativecommons.org/licenses/by-sa/3.0/'),
    ('CC BY', 'by', 'Creative Commons Attribution 3.0 Unported (CC BY 3.0)', 'http://creativecommons.org/licenses/by/3.0/'), 
    ('CC0', 'cc0', 'No Rights Reserved (CC0)', 'http://creativecommons.org/about/cc0'),
)
INFO_PD = (
    ('PD-US', 'pd-us', 'Public Domain, US', 'http://creativecommons.org/about/pdm'),
)
INFO_ALL = INFO_CC + INFO_PD
# CCHOICES, CCGRANTS, and FORMATS are all used in places that expect tuples
# CONTENT_TYPES will be easiest to manipulate in ungluify_record as a dict

CCCHOICES = tuple([(item[0],item[2]) for item in INFO_CC])
    
CHOICES = tuple([(item[0],item[2]) for item in INFO_ALL])

CCGRANTS = tuple([(item[0],item[3]) for item in INFO_CC])

GRANTS = tuple([(item[0],item[3]) for item in INFO_ALL])

LICENSE_LIST =  [item[0] for item in INFO_CC]
LICENSE_LIST_ALL =  [item[0] for item in INFO_ALL]
FACET_LIST = [item[1] for item in INFO_CC] 

class CCLicense():
    @staticmethod
    def url(license):
        if license in LICENSE_LIST_ALL:
            return INFO_ALL[LICENSE_LIST_ALL.index(license)][3]
        else:
            return ''

    @staticmethod
    def badge(license):
        if license == 'PD-US':
            return 'https://i.creativecommons.org/p/mark/1.0/88x31.png'
        elif license == 'CC0':
            return 'https://i.creativecommons.org/p/zero/1.0/88x31.png'
        elif license == 'CC BY':
            return 'https://i.creativecommons.org/l/by/3.0/88x31.png'
        elif license == 'CC BY-NC-ND':
            return 'https://i.creativecommons.org/l/by-nc-nd/3.0/88x31.png'
        elif license == 'CC BY-NC-SA':
            return 'https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png'
        elif license == 'CC BY-NC':
            return 'https://i.creativecommons.org/l/by-nc/3.0/88x31.png'
        elif license == 'CC BY-SA':
            return 'https://i.creativecommons.org/l/by-sa/3.0/88x31.png'
        elif license == 'CC BY-ND':
            return 'https://i.creativecommons.org/l/by-nd/3.0/88x31.png'
        else:
            return ''

def description(license):
        if license == 'PD-US':
            return 'Use of this material is not restricted by copyright in the US.'
        elif license == 'CC0':
            return 'The copyright owner has dedicated the material to the public domain by waiving all of his or her rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law. You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.'
        elif license == 'CC BY':
            return 'You are free to: copy and redistribute the material in any medium or format; remix, transform, and build upon the material; for any purpose, even commercially. Under the following terms: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.'
        elif license == 'CC BY-NC-ND':
            return 'You are free to: copy and redistribute the material in any medium or format; under the following terms: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.; you may not use the material for commercial purposes; if you remix, transform, or build upon the material, you may not distribute the modified material.'
        elif license == 'CC BY-NC-SA':
            return 'You are free to: copy and redistribute the material in any medium or format; remix, transform, and build upon the material; Under the following terms: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use. You may not use the material for commercial purposes. If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.'
        elif license == 'CC BY-NC':
            return 'You are free to: copy and redistribute the material in any medium or format; remix, transform, and build upon the material; under the following terms: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use. You may not use the material for commercial purposes.'
        elif license == 'CC BY-SA':
            return 'You are free to: copy and redistribute the material in any medium or format; remix, transform, and build upon the material; for any purpose, even commercially. Under the following terms: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use. If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.'
        elif license == 'CC BY-ND':
            return 'You are free to: copy and redistribute the material in any medium or format; for any purpose, even commercially. Under the following terms: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use. If you remix, transform, or build upon the material, you may not distribute the modified material.'
        else:
            return ''

class ccinfo():
    def __init__(self, license):
        self.license=license
    
    @property
    def description(self):
        return description(self.license)
    @property
    def badge(self):
        return CCLicense.badge(self.license)
    @property
    def url(self):
        return CCLicense.url(self.license)
    @property
    def title(self):
        if license in LICENSE_LIST_ALL:
            return INFO_ALL[LICENSE_LIST_ALL.index(license)][2]
        else:
            return ''
    