app_sources = [
  'gdict-about.c',
  'gdict-about.h',
  'gdict-app.c',
  'gdict-app.h',
  'gdict-common.c',
  'gdict-common.h',
  'gdict-pref-dialog.c',
  'gdict-pref-dialog.h',
  'gdict-print.c',
  'gdict-print.h',
  'gdict-sidebar.c',
  'gdict-sidebar.h',
  'gdict-source-dialog.c',
  'gdict-source-dialog.h',
  'gdict-window.c',
  'gdict-window.h',
  'main.c',
]

resources = gnome.compile_resources ('gdict-resources',
                                     'gdict.gresource.xml',
                                     source_dir: '.',
                                     c_name: 'gdict')

mathlib = cc.find_library('m', required: false)

executable('gnome-dictionary', app_sources + resources,
           c_args: [
             '-DHAVE_CONFIG_H',
	     '-DPREFIX="@0@"'.format(gdict_prefix),
             '-DSYSCONFDIR="@0@"'.format(gdict_sysconfdir),
             '-DLIBDIR="@0@"'.format(gdict_libdir),
             '-DDATADIR="@0@"'.format(gdict_datadir),
             '-DPKGDATADIR="@0@"'.format(join_paths(gdict_datadir, 'gnome-dictionary')),
             '-DGNOMELOCALEDIR="@0@"'.format(join_paths(gdict_datadir, 'locale')),
           ],
           dependencies: [ libgdict_dep, mathlib ],
           include_directories: [
             root_dir,
             libgdict_inc,
             include_directories('.'),
           ],
           install: true)
