# -*- coding: UTF-8 -*- import cPickle as p #取别名shoplistfile = 'shoplist.data'shoplist =['apple','mango','carrot']f = file(shoplistfile,'w')#写文件到根目录p.dump(shoplist,f)f.close#del shoplistf =file(shoplistfile)storedlist = p.load(f) #加载文件内容print storedlist