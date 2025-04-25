from django.shortcuts import render

def ccmtjal(request):
    texto = '''Com sabedoria, o escritor argentino Jorge Luis Borges, refletindo sobre o homem e o tempo, afirma que “tudo nos diz adeus, tudo nos deixa”. Há, no entanto, segundo ele, algo que se queda, algo que permanece, algo que, de tão relevante, não pode e não deve ser esquecido. São as nossas memórias. Acontecimentos extraordinários que precisam ficar registrados. Um presente do tempo, o modo pelo qual ele, esse tirano incontido, se faz generoso conosco: compensando a efemeridade da vida, nos dá a oportunidade de sermos importantes. E essa importância depende, essencialmente, da capacidade que tenhamos, enquanto povo, de aprender e de ensinar às gerações seguintes, através dos nossos erros, como a escravidão, e acertos, como o Quilombo dos Palmares, onde a alegria e o contentamento misturam-se a dores e horrores, compondo o enredo da nossa história. Somente assim, aprendendo e ensinando, as pegadas deixadas pelo caminho não se apagarão e terão algum sentido. Tudo o mais é caminhar sem direção. Tudo o mais terá sido inútil. Mas, ainda bem que não somos inúteis. Este Centro Cultural e de Memória do Poder Judiciário de Alagoas pretende mostrar um pouco isso. Aqui, guardamos algumas pegadas. Elas nos convidam a olhar criticamente sobre o que fizemos. Que esse olhar nos faça lembrar o quanto de humano, ainda, há em nós.'''
    fotos = [
        "https://images.unsplash.com/photo-1491156855053-9cdff72c7f85?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bXVzZXV8ZW58MHwwfDB8fHwy",
        "https://images.unsplash.com/photo-1554907984-15263bfd63bd?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bXVzZXV8ZW58MHwwfDB8fHwy",
        "https://images.unsplash.com/photo-1514905552197-0610a4d8fd73?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8bXVzZXV8ZW58MHwwfDB8fHwy",
        "https://images.unsplash.com/photo-1637578035851-c5b169722de1?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fG11c2V1fGVufDB8MHwwfHx8Mg%3D%3D",
        "https://images.unsplash.com/photo-1621886292650-520f76c747d6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fG11c2V1fGVufDB8MHwwfHx8Mg%3D%3D",
        "https://images.unsplash.com/photo-1606819717115-9159c900370b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fG11c2V1fGVufDB8MHwwfHx8Mg%3D%3D",
        "https://images.unsplash.com/photo-1524014482380-0988169f598d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fG11c2V1fGVufDB8MHwwfHx8Mg%3D%3D",
        "https://images.unsplash.com/photo-1583306346437-f2143c0f11fc?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fG11c2V1fGVufDB8MHwwfHx8Mg%3D%3D"
    ]
    videos = [
        "lETYY1fCXuE",
        "9iPQa-T7ArQ",
        "ig6p1OJjlhc"
    ]

    return render(request, 'ccmtj/ccmtj/ccmtjal.html', {'texto': texto, 'fotos': fotos, 'videos': videos})