# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ClassificationSpecificEnum(str, Enum):
    """
    
    """

    """
    allowed enum values
    """
    CSX = 'csx'
    CS = 'cs'
    HTML = 'html'
    HTM = 'htm'
    SHTML = 'shtml'
    XHTML = 'xhtml'
    HS = 'hs'
    HS_MINUS_BOOT = 'hs-boot'
    HSIG = 'hsig'
    CPP = 'cpp'
    CC = 'cc'
    CP = 'cp'
    CXX = 'cxx'
    C = 'c'
    H = 'h'
    HH = 'hh'
    HPP = 'hpp'
    HXX = 'hxx'
    INL = 'inl'
    IPP = 'ipp'
    IXX = 'ixx'
    CPPM = 'cppm'
    CSV = 'csv'
    DOC = 'doc'
    DOCM = 'docm'
    DOCX = 'docx'
    EXE = 'exe'
    GIF = 'gif'
    ICO = 'ico'
    JPE = 'jpe'
    JPEG = 'jpeg'
    JPG = 'jpg'
    JPGM = 'jpgm'
    JPGV = 'jpgv'
    LOG = 'log'
    MP2 = 'mp2'
    MP2A = 'mp2a'
    MP3 = 'mp3'
    MP4 = 'mp4'
    MP4A = 'mp4a'
    OGA = 'oga'
    OGG = 'ogg'
    OGV = 'ogv'
    OGX = 'ogx'
    PPT = 'ppt'
    PPTX = 'pptx'
    PPTM = 'pptm'
    QT = 'qt'
    TEXT = 'text'
    TIF = 'tif'
    TIFF = 'tiff'
    TXT = 'txt'
    WAV = 'wav'
    WEBA = 'weba'
    WEBM = 'webm'
    WEBP = 'webp'
    XLA = 'xla'
    XLAM = 'xlam'
    XLC = 'xlc'
    XLM = 'xlm'
    XLS = 'xls'
    XLSB = 'xlsb'
    XLSM = 'xlsm'
    XLSX = 'xlsx'
    XLT = 'xlt'
    XLTM = 'xltm'
    XLTX = 'xltx'
    PDF = 'pdf'
    PNG = 'png'
    RPM = 'rpm'
    ZIP = 'zip'
    WOFF = 'woff'
    WOFF2 = 'woff2'
    SVGZ = 'svgz'
    BIN = 'bin'
    BMP = 'bmp'
    EOT = 'eot'
    GZ = 'gz'
    JAR = 'jar'
    MPKG = 'mpkg'
    AI = 'ai'
    EPS = 'eps'
    DMG = 'dmg'
    LIST = 'list'
    RTX = 'rtx'
    URI = 'uri'
    URIS = 'uris'
    URLS = 'urls'
    CSS = 'css'
    DART = 'dart'
    JAVA = 'java'
    BSH = 'bsh'
    JS = 'js'
    JSX = 'jsx'
    MJS = 'mjs'
    HTC = 'htc'
    JSON = 'json'
    IPYNB = 'ipynb'
    GLTF = 'gltf'
    JSONML = 'jsonml'
    PS = 'ps'
    SSML = 'ssml'
    WASM = 'wasm'
    RTF = 'rtf'
    CCO = 'cco'
    PL = 'pl'
    PC = 'pc'
    PM = 'pm'
    PMC = 'pmc'
    POD = 'pod'
    T = 't'
    XML = 'xml'
    TLD = 'tld'
    DTML = 'dtml'
    RNG = 'rng'
    RSS = 'rss'
    OPML = 'opml'
    SVG = 'svg'
    XAML = 'xaml'
    SUBLIME_MINUS_SNIPPET = 'sublime-snippet'
    TMLANGUAGE = 'tmLanguage'
    TMPREFERENCES = 'tmPreferences'
    TMSNIPPET = 'tmSnippet'
    TMTHEME = 'tmTheme'
    CSPROJ = 'csproj'
    FSPROJ = 'fsproj'
    SQLPROJ = 'sqlproj'
    VBPROJ = 'vbproj'
    VCPROJ = 'vcproj'
    VCXPROJ = 'vcxproj'
    DAE = 'dae'
    PROPS = 'props'
    TARGETS = 'targets'
    XSD = 'xsd'
    XSL = 'xsl'
    XSLT = 'xslt'
    ECMA = 'ecma'
    NODE = 'node'
    PHP = 'php'
    PHP3 = 'php3'
    PHP4 = 'php4'
    PHP5 = 'php5'
    PHP7 = 'php7'
    PHP8 = 'php8'
    PHPS = 'phps'
    PHPT = 'phpt'
    PHTML = 'phtml'
    PY = 'py'
    PY3 = 'py3'
    PYW = 'pyw'
    PYI = 'pyi'
    PYX = 'pyx'
    PYX_DOT_IN = 'pyx.in'
    PXD = 'pxd'
    PXD_DOT_IN = 'pxd.in'
    PXI = 'pxi'
    PXI_DOT_IN = 'pxi.in'
    RPY = 'rpy'
    CPY = 'cpy'
    GYP = 'gyp'
    GYPI = 'gypi'
    VPY = 'vpy'
    SMK = 'smk'
    WSCRIPT = 'wscript'
    BAZEL = 'bazel'
    BZL = 'bzl'
    PYC = 'pyc'
    CLASS = 'class'
    P = 'p'
    PAS = 'pas'
    CURL = 'curl'
    MCURL = 'mcurl'
    GO = 'go'
    SWIFT = 'swift'
    RS = 'rs'
    TS = 'ts'
    TSX = 'tsx'
    RB = 'rb'
    RBI = 'rbi'
    RBX = 'rbx'
    RJS = 'rjs'
    RABL = 'rabl'
    RAKE = 'rake'
    CAPFILE = 'capfile'
    JBUILDER = 'jbuilder'
    GEMSPEC = 'gemspec'
    PODSPEC = 'podspec'
    IRBRC = 'irbrc'
    PRYRC = 'pryrc'
    PRAWN = 'prawn'
    THOR = 'thor'
    APPFILE = 'Appfile'
    APPRAISALS = 'Appraisals'
    BERKSFILE = 'Berksfile'
    BREWFILE = 'Brewfile'
    CHEFFILE = 'Cheffile'
    DELIVERFILE = 'Deliverfile'
    FASTFILE = 'Fastfile'
    GEMFILE = 'Gemfile'
    GUARDFILE = 'Guardfile'
    PODFILE = 'Podfile'
    RAKEFILE = 'Rakefile'
    RANTFILE = 'Rantfile'
    SCANFILE = 'Scanfile'
    SIMPLECOV = 'simplecov'
    SNAPFILE = 'Snapfile'
    THORFILE = 'Thorfile'
    VAGRANTFILE = 'Vagrantfile'
    SCALA = 'scala'
    SBT = 'sbt'
    SC = 'sc'
    CMD = 'cmd'
    BAT = 'bat'
    COFFEE = 'coffee'
    ERL = 'erl'
    HRL = 'hrl'
    ESCRIPT = 'escript'
    LUA = 'lua'
    MD = 'md'
    MDOWN = 'mdown'
    MDWN = 'mdwn'
    MARKDOWN = 'markdown'
    MARKDN = 'markdn'
    MATLAB = 'matlab'
    M = 'm'
    PS1 = 'ps1'
    SH = 'sh'
    BASH = 'bash'
    BASHRC = 'bashrc'
    ASH = 'ash'
    ZSH = 'zsh'
    DOT_BASH_ALIASES = '.bash_aliases'
    DOT_BASH_COMPLETIONS = '.bash_completions'
    DOT_BASH_FUNCTIONS = '.bash_functions'
    DOT_BASH_LOGIN = '.bash_login'
    DOT_BASH_LOGOUT = '.bash_logout'
    DOT_BASH_PROFILE = '.bash_profile'
    DOT_BASH_VARIABLES = '.bash_variables'
    DOT_PROFILE = '.profile'
    DOT_TEXTMATE_INIT = '.textmate_init'
    DOT_ZLOGIN = '.zlogin'
    DOT_ZLOGOUT = '.zlogout'
    DOT_ZPROFILE = '.zprofile'
    DOT_ZSHENV = '.zshenv'
    DOT_ZSHRC = '.zshrc'
    PKGBUILD = 'PKGBUILD'
    EBUILD = 'ebuild'
    ECLASS = 'eclass'
    R = 'r'
    SQL = 'sql'
    DDL = 'ddl'
    DML = 'dml'
    TEX = 'tex'
    LTX = 'ltx'
    STY = 'sty'
    CLS = 'cls'
    UNKNOWN = 'UNKNOWN'
    YAML = 'yaml'
    YML = 'yml'
    TOML = 'toml'
    TML = 'tml'
    CARGO_DOT_LOCK = 'Cargo.lock'
    GOPKG_DOT_LOCK = 'Gopkg.lock'
    PIPFILE = 'Pipfile'
    POETRY_DOT_LOCK = 'poetry.lock'
    UNIFORM_RESOURCE_LOCATOR = 'uniform_resource_locator'
    CUSTOM_URL_SCHEME = 'custom_url_scheme'
    UNIX_FILE_PATH = 'unix_file_path'
    WINDOWS_FILE_PATH = 'windows_file_path'
    UNIFORM_RESOURCE_IDENTIFIER = 'uniform_resource_identifier'
    HLJS_MINUS_1C = 'hljs-1c'
    HLJS_MINUS_ABNF = 'hljs-abnf'
    HLJS_MINUS_ACCESSLOG = 'hljs-accesslog'
    HLJS_MINUS_ACTIONSCRIPT = 'hljs-actionscript'
    HLJS_MINUS_ADA = 'hljs-ada'
    HLJS_MINUS_ANGELSCRIPT = 'hljs-angelscript'
    HLJS_MINUS_APACHE = 'hljs-apache'
    HLJS_MINUS_APPLESCRIPT = 'hljs-applescript'
    HLJS_MINUS_ARCADE = 'hljs-arcade'
    HLJS_MINUS_ARDUINO = 'hljs-arduino'
    HLJS_MINUS_ARMASM = 'hljs-armasm'
    HLJS_MINUS_ASCIIDOC = 'hljs-asciidoc'
    HLJS_MINUS_ASPECTJ = 'hljs-aspectj'
    HLJS_MINUS_AUTOHOTKEY = 'hljs-autohotkey'
    HLJS_MINUS_AUTOIT = 'hljs-autoit'
    HLJS_MINUS_AVRASM = 'hljs-avrasm'
    HLJS_MINUS_AWK = 'hljs-awk'
    HLJS_MINUS_AXAPTA = 'hljs-axapta'
    HLJS_MINUS_BASH = 'hljs-bash'
    HLJS_MINUS_BASIC = 'hljs-basic'
    HLJS_MINUS_BNF = 'hljs-bnf'
    HLJS_MINUS_BRAINFUCK = 'hljs-brainfuck'
    HLJS_MINUS_CAL = 'hljs-cal'
    HLJS_MINUS_CAPNPROTO = 'hljs-capnproto'
    HLJS_MINUS_CEYLON = 'hljs-ceylon'
    HLJS_MINUS_CLEAN = 'hljs-clean'
    HLJS_MINUS_CLOJURE_MINUS_REPL = 'hljs-clojure-repl'
    HLJS_MINUS_CLOJURE = 'hljs-clojure'
    HLJS_MINUS_CMAKE = 'hljs-cmake'
    HLJS_MINUS_COFFEESCRIPT = 'hljs-coffeescript'
    HLJS_MINUS_COQ = 'hljs-coq'
    HLJS_MINUS_COS = 'hljs-cos'
    HLJS_MINUS_CPP = 'hljs-cpp'
    HLJS_MINUS_CRMSH = 'hljs-crmsh'
    HLJS_MINUS_CRYSTAL = 'hljs-crystal'
    HLJS_MINUS_C = 'hljs-c'
    HLJS_MINUS_CS = 'hljs-cs'
    HLJS_MINUS_CSP = 'hljs-csp'
    HLJS_MINUS_CSS = 'hljs-css'
    HLJS_MINUS_D = 'hljs-d'
    HLJS_MINUS_DART = 'hljs-dart'
    HLJS_MINUS_DELPHI = 'hljs-delphi'
    HLJS_MINUS_DIFF = 'hljs-diff'
    HLJS_MINUS_DJANGO = 'hljs-django'
    HLJS_MINUS_DNS = 'hljs-dns'
    HLJS_MINUS_DOCKERFILE = 'hljs-dockerfile'
    HLJS_MINUS_DOS = 'hljs-dos'
    HLJS_MINUS_DSCONFIG = 'hljs-dsconfig'
    HLJS_MINUS_DTS = 'hljs-dts'
    HLJS_MINUS_DUST = 'hljs-dust'
    HLJS_MINUS_EBNF = 'hljs-ebnf'
    HLJS_MINUS_ELIXIR = 'hljs-elixir'
    HLJS_MINUS_ELM = 'hljs-elm'
    HLJS_MINUS_ERB = 'hljs-erb'
    HLJS_MINUS_ERLANG_MINUS_REPL = 'hljs-erlang-repl'
    HLJS_MINUS_ERLANG = 'hljs-erlang'
    HLJS_MINUS_EXCEL = 'hljs-excel'
    HLJS_MINUS_FIX = 'hljs-fix'
    HLJS_MINUS_FLIX = 'hljs-flix'
    HLJS_MINUS_FORTRAN = 'hljs-fortran'
    HLJS_MINUS_FSHARP = 'hljs-fsharp'
    HLJS_MINUS_GAMS = 'hljs-gams'
    HLJS_MINUS_GAUSS = 'hljs-gauss'
    HLJS_MINUS_GCODE = 'hljs-gcode'
    HLJS_MINUS_GHERKIN = 'hljs-gherkin'
    HLJS_MINUS_GLSL = 'hljs-glsl'
    HLJS_MINUS_GML = 'hljs-gml'
    HLJS_MINUS_GO = 'hljs-go'
    HLJS_MINUS_GOLO = 'hljs-golo'
    HLJS_MINUS_GRADLE = 'hljs-gradle'
    HLJS_MINUS_GROOVY = 'hljs-groovy'
    HLJS_MINUS_HAML = 'hljs-haml'
    HLJS_MINUS_HANDLEBARS = 'hljs-handlebars'
    HLJS_MINUS_HASKELL = 'hljs-haskell'
    HLJS_MINUS_HAXE = 'hljs-haxe'
    HLJS_MINUS_HSP = 'hljs-hsp'
    HLJS_MINUS_HTMLBARS = 'hljs-htmlbars'
    HLJS_MINUS_HTTP = 'hljs-http'
    HLJS_MINUS_HY = 'hljs-hy'
    HLJS_MINUS_INFORM7 = 'hljs-inform7'
    HLJS_MINUS_INI = 'hljs-ini'
    HLJS_MINUS_IRPF90 = 'hljs-irpf90'
    HLJS_MINUS_ISBL = 'hljs-isbl'
    HLJS_MINUS_JAVA = 'hljs-java'
    HLJS_MINUS_JAVASCRIPT = 'hljs-javascript'
    HLJS_MINUS_JBOSS_MINUS_CLI = 'hljs-jboss-cli'
    HLJS_MINUS_JSON = 'hljs-json'
    HLJS_MINUS_JULIA_MINUS_REPL = 'hljs-julia-repl'
    HLJS_MINUS_JULIA = 'hljs-julia'
    HLJS_MINUS_KOTLIN = 'hljs-kotlin'
    HLJS_MINUS_LASSO = 'hljs-lasso'
    HLJS_MINUS_LDIF = 'hljs-ldif'
    HLJS_MINUS_LEAF = 'hljs-leaf'
    HLJS_MINUS_LESS = 'hljs-less'
    HLJS_MINUS_LISP = 'hljs-lisp'
    HLJS_MINUS_LIVECODESERVER = 'hljs-livecodeserver'
    HLJS_MINUS_LIVESCRIPT = 'hljs-livescript'
    HLJS_MINUS_LLVM = 'hljs-llvm'
    HLJS_MINUS_LSL = 'hljs-lsl'
    HLJS_MINUS_LUA = 'hljs-lua'
    HLJS_MINUS_MAKEFILE = 'hljs-makefile'
    HLJS_MINUS_MARKDOWN = 'hljs-markdown'
    HLJS_MINUS_MATHEMATICA = 'hljs-mathematica'
    HLJS_MINUS_MATLAB = 'hljs-matlab'
    HLJS_MINUS_MAXIMA = 'hljs-maxima'
    HLJS_MINUS_MEL = 'hljs-mel'
    HLJS_MINUS_MERCURY = 'hljs-mercury'
    HLJS_MINUS_MIPSASM = 'hljs-mipsasm'
    HLJS_MINUS_MIZAR = 'hljs-mizar'
    HLJS_MINUS_MOJOLICIOUS = 'hljs-mojolicious'
    HLJS_MINUS_MONKEY = 'hljs-monkey'
    HLJS_MINUS_MOONSCRIPT = 'hljs-moonscript'
    HLJS_MINUS_N1QL = 'hljs-n1ql'
    HLJS_MINUS_NGINX = 'hljs-nginx'
    HLJS_MINUS_NIMROD = 'hljs-nimrod'
    HLJS_MINUS_NIX = 'hljs-nix'
    HLJS_MINUS_NSIS = 'hljs-nsis'
    HLJS_MINUS_OBJECTIVEC = 'hljs-objectivec'
    HLJS_MINUS_OCAML = 'hljs-ocaml'
    HLJS_MINUS_OPENSCAD = 'hljs-openscad'
    HLJS_MINUS_OXYGENE = 'hljs-oxygene'
    HLJS_MINUS_PARSER3 = 'hljs-parser3'
    HLJS_MINUS_PERL = 'hljs-perl'
    HLJS_MINUS_PF = 'hljs-pf'
    HLJS_MINUS_PGSQL = 'hljs-pgsql'
    HLJS_MINUS_PHP = 'hljs-php'
    HLJS_MINUS_PLAINTEXT = 'hljs-plaintext'
    HLJS_MINUS_PONY = 'hljs-pony'
    HLJS_MINUS_POWERSHELL = 'hljs-powershell'
    HLJS_MINUS_PROCESSING = 'hljs-processing'
    HLJS_MINUS_PROFILE = 'hljs-profile'
    HLJS_MINUS_PROLOG = 'hljs-prolog'
    HLJS_MINUS_PROPERTIES = 'hljs-properties'
    HLJS_MINUS_PROTOBUF = 'hljs-protobuf'
    HLJS_MINUS_PUPPET = 'hljs-puppet'
    HLJS_MINUS_PUREBASIC = 'hljs-purebasic'
    HLJS_MINUS_PYTHON = 'hljs-python'
    HLJS_MINUS_Q = 'hljs-q'
    HLJS_MINUS_QML = 'hljs-qml'
    HLJS_MINUS_R = 'hljs-r'
    HLJS_MINUS_REASONML = 'hljs-reasonml'
    HLJS_MINUS_RIB = 'hljs-rib'
    HLJS_MINUS_ROBOCONF = 'hljs-roboconf'
    HLJS_MINUS_ROUTEROS = 'hljs-routeros'
    HLJS_MINUS_RSL = 'hljs-rsl'
    HLJS_MINUS_RUBY = 'hljs-ruby'
    HLJS_MINUS_RULESLANGUAGE = 'hljs-ruleslanguage'
    HLJS_MINUS_RUST = 'hljs-rust'
    HLJS_MINUS_SAS = 'hljs-sas'
    HLJS_MINUS_SCALA = 'hljs-scala'
    HLJS_MINUS_SCHEME = 'hljs-scheme'
    HLJS_MINUS_SCILAB = 'hljs-scilab'
    HLJS_MINUS_SCSS = 'hljs-scss'
    HLJS_MINUS_SHELL = 'hljs-shell'
    HLJS_MINUS_SMALI = 'hljs-smali'
    HLJS_MINUS_SMALLTALK = 'hljs-smalltalk'
    HLJS_MINUS_SML = 'hljs-sml'
    HLJS_MINUS_SQF = 'hljs-sqf'
    HLJS_MINUS_SQL = 'hljs-sql'
    HLJS_MINUS_STAN = 'hljs-stan'
    HLJS_MINUS_STATA = 'hljs-stata'
    HLJS_MINUS_STEP21 = 'hljs-step21'
    HLJS_MINUS_STYLUS = 'hljs-stylus'
    HLJS_MINUS_SUBUNIT = 'hljs-subunit'
    HLJS_MINUS_SWIFT = 'hljs-swift'
    HLJS_MINUS_TAGGERSCRIPT = 'hljs-taggerscript'
    HLJS_MINUS_TAP = 'hljs-tap'
    HLJS_MINUS_TCL = 'hljs-tcl'
    HLJS_MINUS_TEX = 'hljs-tex'
    HLJS_MINUS_THRIFT = 'hljs-thrift'
    HLJS_MINUS_TP = 'hljs-tp'
    HLJS_MINUS_TWIG = 'hljs-twig'
    HLJS_MINUS_TYPESCRIPT = 'hljs-typescript'
    HLJS_MINUS_VALA = 'hljs-vala'
    HLJS_MINUS_VBNET = 'hljs-vbnet'
    HLJS_MINUS_VBSCRIPT_MINUS_HTML = 'hljs-vbscript-html'
    HLJS_MINUS_VBSCRIPT = 'hljs-vbscript'
    HLJS_MINUS_VERILOG = 'hljs-verilog'
    HLJS_MINUS_VHDL = 'hljs-vhdl'
    HLJS_MINUS_VIM = 'hljs-vim'
    HLJS_MINUS_X86ASM = 'hljs-x86asm'
    HLJS_MINUS_XL = 'hljs-xl'
    HLJS_MINUS_XML = 'hljs-xml'
    HLJS_MINUS_XQUERY = 'hljs-xquery'
    HLJS_MINUS_YAML = 'hljs-yaml'
    HLJS_MINUS_TOML = 'hljs-toml'
    HLJS_MINUS_ZEPHIR = 'hljs-zephir'
    HLJS_MINUS_HTML = 'hljs-html'
    GROOVY = 'groovy'
    KT = 'kt'
    EL = 'el'
    CLJ = 'clj'
    EX = 'ex'
    ADB = 'adb'
    ADS = 'ads'
    AGDA = 'agda'
    ELM = 'elm'
    EXS = 'exs'
    GLSL = 'glsl'
    ML = 'ml'
    LEAN = 'lean'
    LISP = 'lisp'
    RKT = 'rkt'
    SPARQL = 'sparql'
    VHDL = 'vhdl'
    ZIG = 'zig'
    DOCKERFILE = 'dockerfile'
    F03 = 'f03'
    F08 = 'f08'
    F18 = 'f18'
    F90 = 'f90'
    F95 = 'f95'
    JL = 'jl'
    MM = 'mm'
    SCM = 'scm'
    SOL = 'sol'
    SV = 'sv'
    ASP = 'asp'
    CFM = 'cfm'
    FS = 'fs'
    FSI = 'fsi'
    FSX = 'fsx'
    TF = 'tf'
    VBA = 'vba'
    SVELTE = 'svelte'
    VUE = 'vue'
    SCSS = 'scss'
    FEATURE = 'feature'
    INI = 'ini'
    FTL = 'ftl'

    @classmethod
    def from_json(cls, json_str: str) -> ClassificationSpecificEnum:
        """Create an instance of ClassificationSpecificEnum from a JSON string"""
        return ClassificationSpecificEnum(json.loads(json_str))


