import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

bld = Gtk.Builder()
bld.add_from_file("ui.glade")

win = bld.get_object('wnd')

res = bld.get_object('res')

def check(obj):
	try:
		a = int(bld.get_object('inp_a').get_text())
		b = int(bld.get_object('inp_b').get_text())
		c = int(bld.get_object('inp_c').get_text())
	except:
		res.set_text('Неверный ввод. \nПроверьте, чтобы поля не были пустыми \nи введены были \nположительные целые числа')
		return
	else:
		if a + b <= c or a + c <= b or b + c <= a:
			res.set_text('Треугольник с этими сторонами \nне существует')
			return
		else:
			if (a == b == c):
				res.set_text('Треугольник равносторонний')
				return
			elif a == b or b == c or a == c:
				res.set_text('Треугольник равнобедренный')
				return
			elif a**2 + b**2 == c**2:
				res.set_text('Треугольник прямоугольный')
				return
			elif a**2 + b**2 < c**2:
				res.set_text('Треугольник тупоугольный')
				return
			else:
				res.set_text('Треугольник остроугольный')
				return

tab={
	"check_click": check,
	"onDestroy": Gtk.main_quit
}

bld.connect_signals(tab)
win.show_all()

Gtk.main()