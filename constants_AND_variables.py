import tkinter as tk
c_size = 20
c_maxRowSpan = 27
c_maxColumnSpan = 37

s = lambda num: int(c_size * num)

pos = {
    'infoPhoto1':(s(0.5), s(1)),

    'infoPhoto2': (s(0.5), s(6)),

    'infoSelection': (s(2), s(18)),

    'infoOperation': (s(18), s(3)),

    'infoVertices': (s(18), s(9)),

    'photo1': (s(2), s(2)),

    'photo2': (s(2), s(7)),

    'LOGO': (s(2), s(11)),

    'selected': (s(7), s(2)),

    'buttonBack': (s(7), s(15)),

    'buttonNext': (s(14), s(15)),

    'reset': (s(27), s(15)),

    'save': (s(31), s(15)),

    'submit': (s(28), s(18)),

    'folderChoice': (s(23), s(21)),

    'folderDirection': (s(3), s(21)),

    'optionVertices1': (s(19), s(11)),

    'optionVertices2': (s(19), s(13)),
    
    'optionTypeSelection1': (s(9), s(18)),

    'optionTypeSelection2': (s(15), s(18)),

    'optionOperation1': (s(18.8), s(5)),

    'optionOperation2': (s(18.8), s(7)),

    'result': (s(26), s(2)),

    'title': (s(3), s(24))
    }

sizes = {
    'infoPhoto1':(s(6), s(1)),

    'infoPhoto2': (s(6), s(1)),

    'infoSelection': (s(6), s(1)),

    'infoOperation': (s(6), s(1)),

    'infoVertices': (s(6), s(1)),

    'photo1': (s(3), s(3)),

    'photo2': (s(3), s(3)),

    'LOGO': (s(3), s(3)),

    'selected': (s(9), s(12)),

    'buttonBack': (s(2), s(1)),

    'buttonNext': (s(2), s(1)),

    'result': (s(9), s(12)),

    'reset': (s(3), s(2)),

    'save': (s(3), s(2)),

    'submit': (s(5), s(2)),

    'folderChoice': (s(2), s(2)),
    
    'folderDirection': (s(19), s(1)),

    'optionVertices': (s(4), s(1)),
    
    'optionTypeSelection': (s(5), s(1)),

    'optionOperation': (s(4.4), s(1)),

    'title': (s(31), s(2)),

    'window': (str(s(c_maxColumnSpan)) + "x" +str(s(c_maxRowSpan)))
    }

strings = {
    'windowTitle': "Photo Scanner",

    'infoPhoto1': 'David Grajales Grajales',

    'infoPhoto2': 'Juan Calle Jimenez',

    'infoSelection': 'Type Selection:',
    
    'infoOperation': 'Operation:',

    'infoVertices': 'Vertices:',

    'buttonBack': "<<",

    'buttonNext': ">>",

    'reset': 'Reset',

    'save': 'Save',

    'optionVertices1': "Manual",

    'optionVertices2': "Auto",
    
    'optionTypeSelection1': "Directory",

    'optionTypeSelection2': "One Image",

    'optionOperation1': "Ony by One",

    'optionOperation2': "All",

    'submit': 'Submit',
    
    'title': "Photo Scanner"
    }

images = {
    'photo1': "./images/david.jpg",

    "photo2": "./images/juan.jpg",

    "LOGO": "./images/Udea_Escudo.png",

    "selected": "./images/Udea_Escudo.png",

    'folderChoice': "./images/folder.ico",
    }
