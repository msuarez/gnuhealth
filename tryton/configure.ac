AC_INIT([GNU Health], [1.8.1], [health@gnusolidario.org], [GNU Health], [http://health.gnu.org])

AC_PREFIX_DEFAULT(/usr)

AM_PATH_PYTHON([2.7],,)


AC_ARG_WITH(tryton,
[  --with-tryton=PATH      path of tryton server directory],
trytond_path="$withval", trytond_path="no")

if test "$trytond_path" = "no"; then
	TRYTON_PATH=`$PYTHON -c 'from distutils import sysconfig; print sysconfig.get_python_lib()'`
else
	TRYTON_PATH=$trytond_path
fi

TRYTON_MODULES_PATH="$TRYTON_PATH/trytond/modules"

AC_CHECK_FILE($TRYTON_MODULES_PATH,,AC_MSG_ERROR([Tryton modules directory not found. Aborting...]))

AC_SUBST(TRYTON_MODULES_PATH)
	


AC_OUTPUT(Makefile)
