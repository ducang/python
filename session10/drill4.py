while True:
    singer = {
        'Adam Levine' : '''        Adam Noah Levine (born March 18, 1979) is an American singer-songwriter and actor. 
        He is the lead singer for the pop rock band Maroon 5. 
        Born and raised in Los Angeles, California, Levine began his musical career in 1994, 
        when he co-founded the band Kara's Flowers, of which he was the lead vocalist and guitarist.''',
        'Billie Eillish' : '''        Billie Eilish Pirate Baird O'Connell ( born December 18, 2001) is an American singer, songwriter, and model. 
        She gained a following in 2016 when she released her debut single "Ocean Eyes" on audio distribution platform 
        SoundCloud. 
        The single would subsequently be re-released under the record labels Darkroom and Interscope Records.''',
        'Drake' : '''        Aubrey Drake Graham (born October 24, 1986) is a Canadian rapper, singer, songwriter, record producer, actor, and 
        entrepreneur. 
        As an entrepreneur, Drake has founded the OVO Sound record label with longtime collaborator 40. 
        Drake gained recognition as an actor on the teen drama television series Degrassi: The Next Generation 
        in the early 2000s. 
        Intent on pursuing a career in music, he left the series in 2007 after releasing his debut mixtape, 
        Room for Improvement. 
        He released two further independent projects, Comeback Season and So Far Gone, before signing to Lil Wayne's Young Money 
        Entertainment in June 2009.'''
    }

    des = input('Enter a singer or exit to exit:')
    if des.title() in singer:
        print (singer[des.title()])
    elif des in singer:
        print (singer[des])
    elif des == 'exit':
        break
    else:
        print('no information')
   