project('gnome-dictionary', 'c', version: '3.26.1',
        default_options: [
          'buildtype=debugoptimized',
          'c_std=c99',
          'warning_level=1',
        ],
        license: 'GPLv2+',
        meson_version: '>= 0.42.0')

# Paths for the pkg-config file
gdict_prefix = get_option('prefix')
gdict_bindir = join_paths(gdict_prefix, get_option('bindir'))
gdict_libdir = join_paths(gdict_prefix, get_option('libdir'))
gdict_datadir = join_paths(gdict_prefix, get_option('datadir'))
gdict_includedir = join_paths(gdict_prefix, get_option('includedir'))
gdict_libexecdir = join_paths(gdict_prefix, get_option('libexecdir'))
gdict_mandir = join_paths(gdict_prefix, get_option('mandir'))
gdict_sysconfdir = join_paths(gdict_prefix, get_option('sysconfdir'))
gdict_schemadir = join_paths (gdict_datadir, 'glib-2.0', 'schemas')
gdict_servicedir = join_paths (gdict_datadir, 'dbus-1', 'services')

cc = meson.get_compiler('c')
host_system = host_machine.system()

conf = configuration_data()
conf.set_quoted('PACKAGE_NAME', meson.project_name())
conf.set_quoted('PACKAGE_VERSION', meson.project_version())
conf.set_quoted('PACKAGE_STRING', '@0@-@1@'.format(meson.project_name(), meson.project_version()))
conf.set_quoted('PACKAGE_DATADIR', gdict_datadir)
conf.set_quoted('PACKAGE_LIBDIR', gdict_libdir)
conf.set_quoted('PACKAGE_LOCALE_DIR', join_paths(gdict_datadir, 'locale'))
conf.set_quoted('PACKAGE_LIBEXECDIR', gdict_libexecdir)
conf.set('VERSION', 'PACKAGE_VERSION')
conf.set('GETTEXT_PACKAGE', 'PACKAGE_NAME')
conf.set('LOCALEDIR', 'PACKAGE_LOCALE_DIR')
conf.set10('ENABLE_NLS', true) # Always enabled
conf.set('HAVE_UNISTD_H', cc.has_header('unistd.h'))

# Compiler flags
if cc.get_id() == 'gcc' or cc.get_id() == 'clang'
  test_cflags = [
    '-fstrict-aliasing',
    '-Wpointer-arith',
    '-Wmissing-declarations',
    '-Wformat=2',
    '-Wstrict-prototypes',
    '-Wmissing-prototypes',
    '-Wnested-externs',
    '-Wold-style-definition',
    '-Wunused',
    '-Wuninitialized',
    '-Wshadow',
    '-Wmissing-noreturn',
    '-Wmissing-format-attribute',
    '-Wredundant-decls',
    '-Wlogical-op',
    '-Wcast-align',
    '-Wno-unused-local-typedefs',
    '-Werror=implicit',
    '-Werror=init-self',
    '-Werror=main',
    '-Werror=missing-braces',
    '-Werror=return-type',
    '-Werror=array-bounds',
    '-Werror=write-strings'
  ]
else
  test_cflags = []
endif

common_cflags = []
foreach cflag: test_cflags
  if cc.has_argument(cflag)
    common_cflags += [ cflag ]
  endif
endforeach

debug_cflags = []
buildtype = get_option('buildtype')
if buildtype == 'debug'
  debug_cflags += [ '-DGDICT_ENABLE_DEBUG', ]
elif buildtype == 'debugoptimized'
  debug_cflags += [ '-DGDICT_ENABLE_DEBUG', '-DG_DISABLE_CAST_CHECKS', ]
elif buildtype == 'release'
  debug_cflags += [ '-DG_DISABLE_ASSERT', '-DG_DISABLE_CHECKS', '-DG_DISABLE_CAST_CHECKS', ]
endif

ipv6_deps = []

use_ipv6 = get_option('use_ipv6')
if use_ipv6
  ipv6_prog = '''
#include <sys/socket.h>
#include <sys/types.h>

int main (void) {
  struct sockaddr_storage ss;
  socket(AF_INET6, SOCK_STREAM, 0);
  return 0;
}
  '''
  has_ipv6 = cc.compiles(ipv6_prog, name: 'AF_INET6 is available')
  has_getaddrinfo = cc.has_function('getaddrinfo')

  # Look for getaddrinfo in all the known places
  if not has_getaddrinfo
    found_getaddrinfo = false
    foreach l: [ 'bsd', 'socket', 'inet' ]
      dep = cc.find_library(l, required: false)
      if not found_getaddrinfo and dep.found()
        has_getaddrinfo = cc.has_function('getaddrinfo', dependencies: dep)
        if has_getaddrinfo
          ipv6_deps += dep
        endif
      endif
    endforeach
  endif

  use_ipv6 = has_ipv6 and has_getaddrinfo
endif

conf.set10('ENABLE_IPV6', use_ipv6)

root_dir = include_directories('.')
po_dir = join_paths(meson.current_source_dir(), 'po')

configure_file(output: 'config.h', configuration: conf)

gio_dep = dependency('gio-2.0', version: '>= 2.42.0')
gtk_dep = dependency('gtk+-3.0', version: '>= 3.21.2')

gnome = import('gnome')
i18n = import('i18n')

subdir('libgdict')
subdir('src')
subdir('po')
subdir('data')
subdir('help')

# Post-installation trigger
meson.add_install_script ('build-aux/post-install.sh')
