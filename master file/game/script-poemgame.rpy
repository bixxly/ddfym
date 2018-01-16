init python:
    import random

    # This class holds a word, and point values for each of the four heroines
    class PoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, saPoint, sbPoint, naPoint, maPoint, yaPoint, glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint
            self.glitch = glitch
            self.saPoint = saPoint
            self.sbPoint = sbPoint
            self.naPoint = naPoint
            self.maPoint = maPoint
            self.yaPoint = yaPoint

    # Static variables for characters' poem appeal: Disklike, Neutral, Like
    POEM_DISLIKE_THRESHOLD = 29
    POEM_LIKE_THRESHOLD = 45

    # Building the word list
    full_wordlist = []
    with renpy.file('poemwords.txt') as wordfile:
        for line in wordfile:
            # Ignore lines beginning with '#' and empty lines
            line = line.strip()

            if line == '' or line[0] == '#': continue

            # File format: word,sPoint,nPoint,yPoint
            x = line.split(',')
            if (len(x) < 9): continue
            full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3]), float(x[4]), float(x[5]), float(x[6]), float(x[7]), float(x[8])))

    seen_eyes_this_chapter = False
    sayoriTime = renpy.random.random() * 4 + 4
    natsukiTime = renpy.random.random() * 4 + 4
    yuriTime = renpy.random.random() * 4 + 4
    monikaTime = renpy.random.random() * 4 + 4
    sayoriaTime = renpy.random.random() * 4 + 4
    sayoribTime = renpy.random.random() * 4 + 4
    natsukiaTime = renpy.random.random() * 4 + 4
    yuriaTime = renpy.random.random() * 4 + 4
    monikaaTime = renpy.random.random() * 4 + 4
    sayoriPos = 0
    natsukiPos = 0
    yuriPos = 0
    monikaPos = 0
    sayoriaPos = 0
    sayoribPos = 0
    monikaaPos = 0
    natsukiaPos = 0
    yuriPos = 0
    sayoriOffset = 0
    natsukiOffset = 0
    yuriOffset = 0
    monikaOffset = 0
    sayoriaOffset = 0
    sayoribOffset = 0
    monikaaOffset = 0
    natsukiaOffset = 0
    yuriaOffset = 0
    sayoriZoom = 1
    natsukiZoom = 1
    yuriZoom = 1
    monikaZoom = 1
    sayoriaZoom = 1
    sayoribZoom = 1
    monikaaZoom = 1
    natsukiaZoom = 1
    yuriaZoom = 1

    def randomPauseSayori(trans, st, at):
        if st > sayoriTime:
            global sayoriTime
            sayoriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseNatsuki(trans, st, at):
        if st > natsukiTime:
            global natsukiTime
            natsukiTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseYuri(trans, st, at):
        if st > yuriTime:
            global yuriTime
            yuriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseMonika(trans, st, at):
        if st > monikaTime:
            global monikaTime
            monikaTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseSayoria(trans, st, at):
        if st > sayoriaTime:
            global sayoriaTime
            sayoriaTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseSayorib(trans, st, at):
        if st > sayoribTime:
            global sayoribTime
            sayoribTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseMonikaa(trans, st, at):
        if st > monikaaTime:
            global monikaaTime
            monikaaTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseNatsukia(trans, st, at):
        if st > natsukiaTime:
            global natsukiaTime
            natsukiaTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseYuria(trans, st, at):
        if st > yuriaTime:
            global yuriaTime
            yuriaTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomMoveSayori(trans, st, at):
        global sayoriPos
        global sayoriOffset
        global sayoriZoom
        if st > .16:
            if sayoriPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoriPos < 0:
                sayoriPos = renpy.random.randint(0,1)
            else:
                sayoriPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
            return None
        if sayoriPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriPos
        sayoriOffset = trans.xoffset
        sayoriZoom = trans.xzoom
        return 0

    def randomMoveSayoria(trans, st, at):
        global sayoriaPos
        global sayoriaOffset
        global sayoriaZoom
        if st > .16:
            if sayoriaPos > 0:
                sayoriaPos = renpy.random.randint(-1,0)
            elif sayoriaPos < 0:
                sayoriaPos = renpy.random.randint(0,1)
            else:
                sayoriaPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriaPos > 5: sayoriaPos *= -1
            return None
        if sayoriaPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriaPos
        sayoriaOffset = trans.xoffset
        sayoriaZoom = trans.xzoom
        return 0

    def randomMoveSayorib(trans, st, at):
        global sayoribPos
        global sayoribOffset
        global sayoribZoom
        if st > .16:
            if sayoribPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoribPos < 0:
                sayoribPos = renpy.random.randint(0,1)
            else:
                sayoribPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoribPos > 5: sayoribPos *= -1
            return None
        if sayoribPos > 0:
            trans.xzoom = -1
        elif sayoribPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoribPos
        sayoribOffset = trans.xoffset
        sayoribZoom = trans.xzoom
        return 0

    def randomMoveNatsuki(trans, st, at):
        global natsukiPos
        global natsukiOffset
        global natsukiZoom
        if st > .16:
            if natsukiPos > 0:
                natsukiPos = renpy.random.randint(-1,0)
            elif natsukiPos < 0:
                natsukiPos = renpy.random.randint(0,1)
            else:
                natsukiPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
            return None
        if natsukiPos > 0:
            trans.xzoom = -1
        elif natsukiPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiPos
        natsukiOffset = trans.xoffset
        natsukiZoom = trans.xzoom
        return 0

    def randomMoveNatsukia(trans, st, at):
        global natsukiaPos
        global natsukiaOffset
        global natsukiaZoom
        if st > .16:
            if natsukiaPos > 0:
                natsukiaPos = renpy.random.randint(-1,0)
            elif natsukiaPos < 0:
                natsukiaPos = renpy.random.randint(0,1)
            else:
                natsukiaPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiaPos > 5: natsukiaPos *= -1
            return None
        if natsukiaPos > 0:
            trans.xzoom = -1
        elif natsukiaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiaPos
        natsukiaOffset = trans.xoffset
        natsukiaZoom = trans.xzoom
        return 0

    def randomMoveYuri(trans, st, at):
        global yuriPos
        global yuriOffset
        global yuriZoom
        if st > .16:
            if yuriPos > 0:
                yuriPos = renpy.random.randint(-1,0)
            elif yuriPos < 0:
                yuriPos = renpy.random.randint(0,1)
            else:
                yuriPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriPos > 5: yuriPos *= -1
            return None
        if yuriPos > 0:
            trans.xzoom = -1
        elif yuriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriPos
        yuriOffset = trans.xoffset
        yuriZoom = trans.xzoom
        return 0

    def randomMoveYuria(trans, st, at):
        global yuriaPos
        global yuriaOffset
        global yuriaZoom
        if st > .16:
            if yuriaPos > 0:
                yuriaPos = renpy.random.randint(-1,0)
            elif yuriaPos < 0:
                yuriaPos = renpy.random.randint(0,1)
            else:
                yuriaPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriaPos > 5: yuriaPos *= -1
            return None
        if yuriaPos > 0:
            trans.xzoom = -1
        elif yuriaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriaPos
        yuriaOffset = trans.xoffset
        yuriaZoom = trans.xzoom
        return 0

    def randomMoveMonika(trans, st, at):
        global monikaPos
        global monikaOffset
        global monikaZoom
        if st > .16:
            if monikaPos > 0:
                monikaPos = renpy.random.randint(-1,0)
            elif monikaPos < 0:
                monikaPos = renpy.random.randint(0,1)
            else:
                monikaPos = renpy.random.randint(-1,1)
            if trans.xoffset * monikaPos > 5: monikaPos *= -1
            return None
        if monikaPos > 0:
            trans.xzoom = -1
        elif monikaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * monikaPos
        monikaOffset = trans.xoffset
        monikaZoom = trans.xzoom
        return 0

    def randomMoveMonikaa(trans, st, at):
        global monikaaPos
        global monikaaOffset
        global monikaaZoom
        if st > .16:
            if monikaaPos > 0:
                monikaaPos = renpy.random.randint(-1,0)
            elif monikaaPos < 0:
                monikaaPos = renpy.random.randint(0,1)
            else:
                monikaaPos = renpy.random.randint(-1,1)
            if trans.xoffset * monikaaPos > 5: monikaaPos *= -1
            return None
        if monikaaPos > 0:
            trans.xzoom = -1
        elif monikaaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * monikaaPos
        monikaaOffset = trans.xoffset
        monikaaZoom = trans.xzoom
        return 0


label poem(transition=True):
    stop music fadeout 2.0
    if persistent.playthrough == 3:
        scene bg notebook-glitch
    else:
        scene bg notebook
    show screen quick_menu
    #Doki shuffling
    python:
        topRowDokis = []
        midRowDokis = []
        botRowDokis = []
        botPoses = [sticker_left, sticker_mid, sticker_right]
        midPoses = [mid_sticker_left, mid_sticker_mid, mid_sticker_right]
        topPoses = [top_sticker_left, top_sticker_mid, top_sticker_right]
        unassignedDokis = ["Sayori", "Natsuki", "Yuri", "Sayoria", "Sayorib", "Natsukia", "Monikaa", "Yuria"]
        if persistent.playthrough == 3:
            unassignedDokis.append("Monika")
        random.shuffle(unassignedDokis)
    if persistent.playthrough is not 0:
            $ unassignedDokis.remove("Sayori")
    python:
        for doki in unassignedDokis:
            if len(botRowDokis) < 3:
                botRowDokis.append(doki)
            elif len(midRowDokis) < 3:
                midRowDokis.append(doki)
            else:
                topRowDokis.append(doki)
    #Bottom Row Doki Placement
    $ i = 0
    label bRowLoop:
        $ jumper = 0
        while i<3:
            python:
                if len(botRowDokis) >= i+1:
                    doki = botRowDokis[i]
                else:
                    i+=1
                    jumper = 1
            if jumper == 1:
                jump bRowLoop
            if doki == "Sayori":
                show s_sticker at botPoses[i]
            if doki == "Sayoria":
                show sa_sticker at botPoses[i]
            if doki == "Sayorib":
                show sb_sticker at botPoses[i]

            if doki == "Natsuki":
                show n_sticker at botPoses[i]
            if doki == "Natsukia":
                show na_sticker at botPoses[i]

            if doki == "Monika":
                show m_sticker at botPoses[i]
            if doki == "Monikaa":
                show ma_sticker at botPoses[i]

            if doki == "Yuri":
                if persistent.playthrough == 2 and chapter == 2:
                    show y_sticker_cut at botPoses[i]
                else:
                    show y_sticker at botPoses[i]
            if doki == "Yuria":
                show ya_sticker at botPoses[i]
            $ i+=1

    #Mid Row Doki Placement
    $ i = 0
    label mRowLoop:
        $ jumper = 0
        while i < 3:
            python:
                if len(midRowDokis) >= i+1:
                    doki = midRowDokis[i]
                else:
                    i+=1
                    jumper = 1
            if jumper == 1:
                jump mRowLoop
            if doki == "Sayori":
                show s_sticker at midPoses[i]
            if doki == "Sayoria":
                show sa_sticker at midPoses[i]
            if doki == "Sayorib":
                show sb_sticker at midPoses[i]

            if doki == "Natsuki":
                show n_sticker at midPoses[i]
            if doki == "Natsukia":
                show na_sticker at midPoses[i]

            if doki == "Monika":
                show m_sticker at midPoses[i]
            if doki == "Monikaa":
                show ma_sticker at midPoses[i]

            if doki == "Yuri":
                if persistent.playthrough == 2 and chapter == 2:
                    show y_sticker_cut at midPoses[i]
                else:
                    show y_sticker at midPoses[i]
            if doki == "Yuria":
                show ya_sticker at botPoses[i] 
            $ i+=1

    #Top Row Doki Placement
    $ i = 0
    label tRowLoop:
        $ jumper = 0
        while i < 3:
            python:
                if len(topRowDokis) >= i+1:
                    doki = topRowDokis[i]
                else:
                    i += 1
                    jumper = 1
            if jumper == 1:
                jump tRowLoop
            if doki == "Sayori":
                show s_sticker at topPoses[i]
            if doki == "Sayoria":
                show sa_sticker at topPoses[i]
            if doki == "Sayorib":
                show sb_sticker at topPoses[i]

            if doki == "Natsuki":
                show n_sticker at topPoses[i]
            if doki == "Natsukia":
                show na_sticker at topPoses[i]

            if doki == "Monika":
               show m_sticker at topPoses[i]
            if doki == "Monikaa":
                show ma_sticker at topPoses[i]

            if doki == "Yuri":
                if persistent.playthrough == 2 and chapter == 2:
                    show y_sticker_cut at topPoses[i]
                else:
                    show y_sticker at topPoses[i]
            if doki == "Yuria":
                show ya_sticker at topPoses[i]
            $ i+=1

        if persistent.playthrough == 2 and chapter == 2:
            show m_sticker at sticker_m_glitch
    if transition:
        with dissolve_scene_full
    if persistent.playthrough == 3:
        play music ghostmenu
    else:
        play music t4
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    if persistent.playthrough == 0 and chapter == 0:
        call screen dialog("It's time to write a poem!\n\nPick words you think your favorite club member\nwill like. Something good might happen with\nwhoever likes your poem the most!", ok_action=Return())
    python:
        poemgame_glitch = False
        played_baa = False
        progress = 1
        numWords = 20
        sPointTotal = 0
        nPointTotal = 0
        yPointTotal = 0
        saPointTotal = 0
        sbPointTotal = 0
        naPointTotal = 0
        yaPointTotal = 0
        maPointTotal = 0
        wordlist = list(full_wordlist)

        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        sayoriaTime = renpy.random.random() * 4 + 4
        sayoribTime = renpy.random.random() * 4 + 4
        natsukiaTime = renpy.random.random() * 4 + 4
        yuriaTime = renpy.random.random() * 4 + 4
        monikaaTime = renpy.random.random() * 4 + 4
        sayoriPos = renpy.random.randint(-1,1)
        natsukiPos = renpy.random.randint(-1,1)
        yuriPos = renpy.random.randint(-1,1)
        sayoriaPos = renpy.random.randint(-1,1)
        sayoribPos = renpy.random.randint(-1,1)
        natsukiaPos = renpy.random.randint(-1,1)
        yuriaPos = renpy.random.randint(-1,1)
        monikaaTime = renpy.random.randint(-1,1)
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        sayoriaOffset = 0
        sayoribOffset = 0
        natsukiaOffset = 0
        yuriaOffset = 0
        monikaaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        sayoriaZoom = 1
        sayoribZoom = 1
        natsukiaZoom = 1
        yuriaZoom = 1
        monikaaZoom = 1


        # Main loop for drawing and selecting words
        while True:
            ystart = 160
            if persistent.playthrough == 2 and chapter == 2:
                pstring = ""
                for i in range(progress):
                    pstring += "1"
            else:
                pstring = str(progress)
            ui.text(pstring + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000')
            for j in range(2):
                if j == 0: x = 440
                else: x = 680
                ui.vbox()
                for i in range(5):
                    if persistent.playthrough == 3:
                        s = list("Monika")
                        for k in range(6):
                            if random.randint(0, 4) == 0:
                                s[k] = ' '
                            elif random.randint(0, 4) == 0:
                                s[k] = random.choice(nonunicode)
                        word = PoemWord("".join(s), 0, 0, 0, 0, 0, 0, 0, 0, False)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        word = PoemWord(glitchtext(80), 0, 0, 0, 0, 0, 0, 0, 0, True)
                    else:
                        word = random.choice(wordlist)
                        wordlist.remove(word)
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                ui.close()

            t = ui.interact()
            if not poemgame_glitch:
                if t.glitch:
                    poemgame_glitch = True
                    renpy.music.play(audio.t4g)
                    renpy.scene()
                    renpy.show("white")
                    renpy.show("y_sticker glitch", at_list=[sticker_glitch])
                elif persistent.playthrough != 3:
                    renpy.play(gui.activate_sound)
                    if persistent.playthrough == 0:
                        if t.sPoint >= 3:
                            renpy.show("s_sticker hop")
                        if t.nPoint >= 3:
                            renpy.show("n_sticker hop")
                        if t.yPoint >= 3:
                            renpy.show("y_sticker hop")
                        if t.saPoint >= 3:
                            renpy.show("sa_sticker hop")
                        if t.sbPoint >= 3:
                            renpy.show("sb_sticker hop")
                        if t.naPoint >= 3:
                            renpy.show("na_sticker hop")
                        if t.yaPoint >= 3:
                            renpy.show("ya_sticker hop")
                        if t.maPoint >= 3:
                            renpy.show("ma_sticker hop")
                    else:
                        if persistent.playthrough == 2 and chapter == 2 and random.randint(0,10) == 0: renpy.show("m_sticker hop")
                        elif t.nPoint > t.yPoint: renpy.show("n_sticker hop")
                        elif t.naPoint > t.yPoint: renpy.show("na_sticker hop")
                        elif t.saPoint > t.yPoint: renpy.show("sa_sticker hop")
                        elif t.sbPoint > t.yPoint: renpy.show("sb_sticker hop")
                        elif t.yaPoint > t.yPoint: renpy.show("ya_sticker hop")
                        elif t.maPoint > t.yPoint: renpy.show("ma_sticker hop")
                        elif persistent.playthrough == 2 and not persistent.seen_sticker and random.randint(0,100) == 0:
                            renpy.show("y_sticker hopg")
                            persistent.seen_sticker = True
                        elif persistent.playthrough == 2 and chapter == 2: renpy.show("y_sticker_cut hop")
                        else: renpy.show("y_sticker hop")
            else:
                r = random.randint(0, 10)
                if r == 0 and not played_baa:
                    renpy.play("gui/sfx/baa.ogg")
                    played_baa = True
                elif r <= 5: renpy.play(gui.activate_sound_glitch)
            sPointTotal += t.sPoint
            nPointTotal += t.nPoint
            yPointTotal += t.yPoint
            saPointTotal += t.saPoint
            sbPointTotal += t.sbPoint
            naPointTotal += t.naPoint
            yaPointTotal += t.yaPoint
            maPointTotal += t.maPoint
            progress += 1
            if progress > numWords:
                break

        if persistent.playthrough == 0:
            # For chapter 1, add 5 points to whomever we sided with
            if chapter == 1:
                exec(ch1_choice[0] + "PointTotal += 5")
            # Logic for taking point totals and assigning poem appeal, scene order, etc.
            unsorted_pointlist = {"sayori": sPointTotal, "natsuki": nPointTotal, "yuri": yPointTotal}
            pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)

            # Set poemwinner to the highest scorer
            poemwinner[chapter] = pointlist[2]
        else:
            if nPointTotal > yPointTotal: poemwinner[chapter] = "natsuki"
            else: poemwinner[chapter] = "yuri"

        # Add appeal point based on poem winner
        exec(poemwinner[chapter][0] + "_appeal += 1")

        # Set poemappeal
        if sPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal[chapter] = -1
        elif sPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal[chapter] = 1
        if nPointTotal < POEM_DISLIKE_THRESHOLD: n_poemappeal[chapter] = -1
        elif nPointTotal > POEM_LIKE_THRESHOLD: n_poemappeal[chapter] = 1
        if yPointTotal < POEM_DISLIKE_THRESHOLD: y_poemappeal[chapter] = -1
        elif yPointTotal > POEM_LIKE_THRESHOLD: y_poemappeal[chapter] = 1

        # Poem winner always has appeal 1 (loves poem)
        exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")

    if persistent.playthrough == 2 and persistent.seen_eyes == None and renpy.random.randint(0,5) == 0:
        $ seen_eyes_this_chapter = True
        $ quick_menu = False
        play sound "sfx/eyes.ogg"
        $ persistent.seen_eyes = True
        stop music
        scene black with None
        show bg eyes_move
        pause 1.2
        hide bg eyes_move
        show bg eyes
        pause 0.5
        hide bg eyes
        show bg eyes_move
        pause 1.25
        hide bg eyes with None
        $ quick_menu = True
    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music fadeout 2.0
    hide screen quick_menu
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return

image bg eyes_move:
    "images/bg/eyes.png"
    parallel:
        yoffset 720 ytile 2
        linear 0.5 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat
image bg eyes:
    "images/bg/eyes.png"

image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image sa_sticker:
    "mod-assets/fylc/sayoria1.png"
    xoffset sayoriaOffset xzoom sayoriaZoom
    block:
        function randomPauseSayoria
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayoria
        repeat

image sb_sticker:
    "mod-assets/fylc/sayorib1.png"
    xoffset sayoribOffset xzoom sayoribZoom
    block:
        function randomPauseSayorib
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayorib
        repeat

image ma_sticker:
    "mod-assets/fylc/monika1.png"
    xoffset monikaaOffset xzoom monikaaZoom
    block:
        function randomPauseMonikaa
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonikaa
        repeat

image na_sticker:
    "mod-assets/fylc/natsuki1.png"
    xoffset natsukiaOffset xzoom natsukiaZoom
    block:
        function randomPauseNatsukia
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsukia
        repeat

image ya_sticker:
    "mod-assets/fylc/yuri1.png"
    xoffset yuriaOffset xzoom yuriaZoom
    block:
        function randomPauseYuria
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuria
        repeat


image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    "gui/poemgame/m_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset yuriOffset xzoom yuriZoom zoom 3.0
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image sa_sticker hop:
    "mod-assets/fylc/sayoria2.png"
    xoffset sayoriaOffset xzoom sayoriaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "sa_sticker"

image sb_sticker hop:
    "mod-assets/fylc/sayorib2.png"
    xoffset sayoribOffset xzoom sayoribZoom
    sticker_hop
    xoffset 0 xzoom 1
    "sb_sticker"

image ma_sticker hop:
    "mod-assets/fylc/monika2.png"
    xoffset monikaaOffset xzoom monikaaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "ma_sticker"

image na_sticker hop:
    "mod-assets/fylc/natsuki2.png"
    xoffset natsukiaOffset xzoom natsukiaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "na_sticker"

image ya_sticker hop:
    "mod-assets/fylc/yuri2.png"
    xoffset yuriaOffset xzoom yuriaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "ya_sticker"

transform sticker_left:
    xcenter 100 yalign 0.9 subpixel True

transform sticker_mid:
    xcenter 220 yalign 0.9 subpixel True

transform sticker_right:
    xcenter 340 yalign 0.9 subpixel True

transform sticker_glitch:
    xcenter 50 yalign 1.8 subpixel True

transform sticker_m_glitch:
    xcenter 100 yalign 1.35 subpixel True

transform mid_sticker_left:
    xcenter 100 yalign 0.5 subpixel True

transform mid_sticker_mid:
    xcenter 220 yalign 0.5 subpixel True

transform mid_sticker_right:
    xcenter 340 yalign 0.5 subpixel True

transform top_sticker_left:
    xcenter 100 yalign 0.1 subpixel True

transform top_sticker_mid:
    xcenter 220 yalign 0.1 subpixel True

transform top_sticker_right:
    xcenter 340 yalign 0.1 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
