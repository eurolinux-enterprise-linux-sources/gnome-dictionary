sources_h = [
  'gdict-context.h',
  'gdict-client-context.h',
  'gdict-database-chooser.h',
  'gdict-database-chooser-button.h',
  'gdict-defbox.h',
  'gdict-source-chooser.h',
  'gdict-source-loader.h',
  'gdict-source.h',
  'gdict-speller.h',
  'gdict-strategy-chooser.h',
  'gdict-utils.h',
]

sources_h_priv = [
  'gdict-context-private.h',
  'gdict-debug.h',
  'gdict-private.h',
]

sources_c = [
  'gdict-context.c',
  'gdict-client-context.c',
  'gdict-database-chooser.c',
  'gdict-database-chooser-button.c',
  'gdict-defbox.c',
  'gdict-source-chooser.c',
  'gdict-source-loader.c',
  'gdict-source.c',
  'gdict-speller.c',
  'gdict-strategy-chooser.c',
  'gdict-utils.c',
]

libgdict_enums = gnome.mkenums('gdict-enum-types', sources: sources_h,
                               h_template: 'gdict-enum-types.h.in',
                               c_template: 'gdict-enum-types.c.in',
                               install_header: false)
libgdict_marshal = gnome.genmarshal('gdict-marshal',
                                    sources: 'gdict-marshal.list',
                                    prefix: 'gdict_marshal')

libgdict_version = meson.project_version().split('.')
libgdict_major = libgdict_version[0].to_int()
libgdict_minor = libgdict_version[1].to_int()
libgdict_micro = libgdict_version[2].to_int()

libgdict_cflags = [
  '-DHAVE_CONFIG_H',
  '-D_GNU_SOURCE',
  '-DG_LOG_DOMAIN="Gdict"',
  '-DDATADIR="@0@"'.format(gdict_datadir),
  '-DLIBDIR="@0@"'.format(gdict_libdir),
  '-DSYSCONFDIR="@0@"'.format(gdict_sysconfdir),
  '-DPREFIX="@0@"'.format(gdict_prefix),
  '-DGNOMELOCALEDIR="@0@"'.format(join_paths(gdict_datadir, 'locale')),
  '-DGDICTSOURCESDIR="@0@"'.format(join_paths(gdict_datadir, 'gdict-1.0', 'sources')),
  '-DGDICT_ENABLE_INTERNALS=1',
  '-DGDICT_MAJOR_VERSION=@0@'.format(libgdict_major),
  '-DGDICT_MINOR_VERSION=@0@'.format(libgdict_minor),
  '-DGDICT_MICRO_VERSION=@0@'.format(libgdict_micro),
  '-DG_DISABLE_DEPRECATED',
  '-DGDK_DISABLE_DEPRECATED',
  '-UGTK_DISABLE_DEPRECATED',
  '-DPANGO_DISABLE_DEPRECATED',
  '-DG_DISABLE_SINGLE_INCLUDES',
  '-DGTK_DISABLE_SINGLE_INCLUDES',
]

libgdict_ldflags = []
if cc.get_id() == 'gcc'
  libgdict_ldflags += [
    '-Wl,-Bsymbolic-functions',
    '-Wl,-z,relro',
    '-Wl,-z,now',
  ]
endif

libgdict_inc = include_directories('.')

libgdict_lib = static_library('libgdict-1.0',
                              sources: sources_h_priv + sources_c + libgdict_enums + libgdict_marshal,
                              dependencies: [ gio_dep, gtk_dep, ipv6_deps ],
                              include_directories: [ root_dir, libgdict_inc ],
                              c_args: common_cflags + debug_cflags + libgdict_cflags,
                              link_args: libgdict_ldflags,
                              install: false)

libgdict_dep = declare_dependency(sources: libgdict_enums + libgdict_marshal,
                                  link_with: libgdict_lib,
				  include_directories: [ libgdict_inc ],
				  dependencies: [ gio_dep, gtk_dep, ipv6_deps ])
