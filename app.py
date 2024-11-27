import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

bld = Gtk.Builder()
bld.add_from_file("ui.glade")

win = bld.get_object('wnd')

res = bld.get_object('res')

inpa = bld.get_object('inp_a')
inpb = bld.get_object('inp_b')
inpc = bld.get_object('inp_c')

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
			else:
				res.set_text('Треугольник разносторонний')
				return

def cls_vals(obj):
	inpa.set_text('')
	inpb.set_text('')
	inpc.set_text('')

tab={
	"check_click": check,
	"onDestroy": Gtk.main_quit,
	"clear_inp": cls_vals
}

bld.connect_signals(tab)
win.show_all()

Gtk.main()