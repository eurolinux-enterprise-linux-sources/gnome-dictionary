
#ifndef __gdict_marshal_MARSHAL_H__
#define __gdict_marshal_MARSHAL_H__

#include	<glib-object.h>

G_BEGIN_DECLS

/* VOID:VOID (./gdict-marshal.list:1) */
#define gdict_marshal_VOID__VOID	g_cclosure_marshal_VOID__VOID

/* VOID:POINTER (./gdict-marshal.list:2) */
#define gdict_marshal_VOID__POINTER	g_cclosure_marshal_VOID__POINTER

/* VOID:BOXED (./gdict-marshal.list:3) */
#define gdict_marshal_VOID__BOXED	g_cclosure_marshal_VOID__BOXED

/* VOID:OBJECT (./gdict-marshal.list:4) */
#define gdict_marshal_VOID__OBJECT	g_cclosure_marshal_VOID__OBJECT

/* VOID:STRING (./gdict-marshal.list:5) */
#define gdict_marshal_VOID__STRING	g_cclosure_marshal_VOID__STRING

/* VOID:STRING,STRING (./gdict-marshal.list:6) */
extern void gdict_marshal_VOID__STRING_STRING (GClosure     *closure,
                                               GValue       *return_value,
                                               guint         n_param_values,
                                               const GValue *param_values,
                                               gpointer      invocation_hint,
                                               gpointer      marshal_data);

/* VOID:STRING,OBJECT (./gdict-marshal.list:7) */
extern void gdict_marshal_VOID__STRING_OBJECT (GClosure     *closure,
                                               GValue       *return_value,
                                               guint         n_param_values,
                                               const GValue *param_values,
                                               gpointer      invocation_hint,
                                               gpointer      marshal_data);

G_END_DECLS

#endif /* __gdict_marshal_MARSHAL_H__ */

