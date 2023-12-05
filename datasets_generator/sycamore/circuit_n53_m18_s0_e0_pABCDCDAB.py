import cirq
import numpy as np

QUBIT_ORDER = [
    cirq.GridQubit(0, 5),
    cirq.GridQubit(0, 6),
    cirq.GridQubit(1, 4),
    cirq.GridQubit(1, 5),
    cirq.GridQubit(1, 6),
    cirq.GridQubit(1, 7),
    cirq.GridQubit(2, 4),
    cirq.GridQubit(2, 5),
    cirq.GridQubit(2, 6),
    cirq.GridQubit(2, 7),
    cirq.GridQubit(2, 8),
    cirq.GridQubit(3, 2),
    cirq.GridQubit(3, 3),
    cirq.GridQubit(3, 4),
    cirq.GridQubit(3, 5),
    cirq.GridQubit(3, 6),
    cirq.GridQubit(3, 7),
    cirq.GridQubit(3, 8),
    cirq.GridQubit(3, 9),
    cirq.GridQubit(4, 1),
    cirq.GridQubit(4, 2),
    cirq.GridQubit(4, 3),
    cirq.GridQubit(4, 4),
    cirq.GridQubit(4, 5),
    cirq.GridQubit(4, 6),
    cirq.GridQubit(4, 7),
    cirq.GridQubit(4, 8),
    cirq.GridQubit(4, 9),
    cirq.GridQubit(5, 0),
    cirq.GridQubit(5, 1),
    cirq.GridQubit(5, 2),
    cirq.GridQubit(5, 3),
    cirq.GridQubit(5, 4),
    cirq.GridQubit(5, 5),
    cirq.GridQubit(5, 6),
    cirq.GridQubit(5, 7),
    cirq.GridQubit(5, 8),
    cirq.GridQubit(6, 1),
    cirq.GridQubit(6, 2),
    cirq.GridQubit(6, 3),
    cirq.GridQubit(6, 4),
    cirq.GridQubit(6, 5),
    cirq.GridQubit(6, 6),
    cirq.GridQubit(6, 7),
    cirq.GridQubit(7, 2),
    cirq.GridQubit(7, 3),
    cirq.GridQubit(7, 4),
    cirq.GridQubit(7, 5),
    cirq.GridQubit(7, 6),
    cirq.GridQubit(8, 3),
    cirq.GridQubit(8, 4),
    cirq.GridQubit(8, 5),
    cirq.GridQubit(9, 4),
]

CIRCUIT = cirq.Circuit(
    [
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.7743385483953005).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -0.7085204779284944).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.8687711187158653).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.3853766657859231).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.3522159558487364).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 0.569527381436443).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.06748036788071975).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -0.03542260032736748).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.921123478965347).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.940605149780575).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.40878079457469985).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -0.3573777822597026).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.4286328898578044).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.567173927172081).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 0.6962362636582926).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.6243336356713873).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.5070267688233168).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.49025706927611445).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.82479487914479).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * 0.831505604695568).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.7654710267272109).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.7622667609489339).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.7530995459405583).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.7063901684965722).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.7750964509509387).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.9619956872914577).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.8310454946335954).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.8149432193242095).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.568448771120722).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.5458328527656618).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 0.46444025457872556).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.8641681946768033).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.33639050361710615).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.4121311900075394).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.881176970884841).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.8199816956867351).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -0.5174631371535426).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.5093922035705379).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -0.2684453761112637).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.26751780455859997).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.7883616255904944).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.9304903862480522).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 0.5471409474788239).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.5891117186780521).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 0.7384907660505857).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.7451407522809496).on(cirq.GridQubit(8, 5)),
                cirq.Rz(np.pi * -0.1830293948567971).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * -0.1757017537984857).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5157741664069029, phi=0.5567125777723744).on(
                    cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5177580142209797, phi=0.4948108578225166).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.6036738621219824, phi=0.47689957001758815).on(
                    cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5177327089642791, phi=0.5058312223892585).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5253184444076096, phi=0.46557175536519374).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.6141004604574274, phi=0.494343440675308).on(
                    cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.5476810407275208, phi=0.44290174465702487).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5237261387830179, phi=0.4696616122846161).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5285844942020295, phi=0.5736654641906893).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5483159975149505, phi=0.4961408893973623).on(
                    cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.6377079485605028, phi=0.6888985951517526).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.529949914236052, phi=0.48258847574702635).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5280421758407217, phi=0.5109767145462891).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5120782868771674, phi=0.4815152809861558).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5071938854285831, phi=0.5089276063739265).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)
                ),
                cirq.FSimGate(theta=1.5460100224551203, phi=0.5302403303961576).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5166625940397171, phi=0.4517159790427676).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.4597689731864314, phi=0.4214985958536156).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.535649445690472, phi=0.47076284376181704).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)
                ),
                cirq.FSimGate(theta=1.5179778495708582, phi=0.5221350266177334).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.4969321270213238, phi=0.4326117171327162).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.5114987201637704, phi=0.4914319343687703).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)
                ),
                cirq.FSimGate(theta=1.4908807480930255, phi=0.4886243720131578).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)
                ),
                cirq.FSimGate(theta=1.616256999726831, phi=0.501428936283957).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.7618064157555159).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 0.827624486222322).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.677790595837605).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.8388149512324528).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.34915411632258214).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -0.13184269073487556).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.4610625765182105).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -0.4290048089648583).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.6641998401797986).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.6836815109950266).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.026240452181357746).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 0.025162560133639312).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.9071761579568303).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.9542828047288932).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.46145806100291004).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.5333606889898155).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.5128100748460089).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.4960403752988061).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.5829645187562967).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -0.5762537932055181).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.022811401598836913).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.019607135820559906).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.8523020333228131).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.8990114107667992).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.9352866185158868).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.7483873821753678).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.9220101925888569).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.9059079172794712).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.7039221690166656).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.6813062506616053).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 0.6965073865506469).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.9037646733512754).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.45310524873049973).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.3773645623400665).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.42017342300456634).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.3589781478064599).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 0.9534707755965702).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.9615417091795746).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 0.5368636250628501).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.5377911966155139).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.5123942238917779).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.7935422120532315).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * -0.7898684772427236).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.7478977060434954).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -0.8571455144841159).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.8504955282537521).on(cirq.GridQubit(8, 5)),
                cirq.Rz(np.pi * 0.9094649565590708).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * 0.7318038947856463).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 9)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.07221640979880403).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 0.17734365608174887).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.7166427083722222).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 0.717673588252228).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -0.1312926423470736).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.13158529074665537).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.7500367576549269).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.31797150857789674).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.8756735306896725).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.9327732133062662).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.7071565092929694).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -0.6264998637477406).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.82790347048799).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.8594778743809006).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.8064559428449068).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.7629602352736249).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.23630732076940514).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.25438180016733336).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.6476084230939583).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -0.6528339440806201).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.20879565669998532).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.26053049452558324).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.7777343640360711).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.8805385932920736).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.5137630264839785).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.48179097076948874).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.7693840211762448).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.7680082232923118).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.14188452450562264).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.1339396318115881).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.95616894502165).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.9015807139989003).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.3168365530459615).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.2898226701533191).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.32361247881294825).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.27931184143712456).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.884543382731205).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.8540367322639986).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5192859850645715, phi=0.49387245572956845).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5120572609259932, phi=0.5211713721957417).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)
                ),
                cirq.FSimGate(theta=1.615096254724942, phi=0.7269644142795206).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5269188098932545, phi=0.5036266469194081).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5179602369002039, phi=0.4914328237769214).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.537427483096926, phi=0.45115204759967975).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.53486366638317, phi=0.46559889697604934).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5194586006330344, phi=0.5068560732280918).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5819908111894527, phi=0.5595875596558442).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.5070579127771144, phi=0.4520319437379419).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.527311970249325, phi=0.4920204543143157).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5139592614725292, phi=0.45916943035876673).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5425204049671604, phi=0.5057437054391503).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.5432564804093452, phi=0.5658780292653538).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.4611081680611278, phi=0.5435451345370095).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.4529959991143482, phi=0.43830813863531964).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.6239619425876082, phi=0.4985036227887135).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.4884560669186362, phi=0.4964777432807688).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5034760541420213, phi=0.5004774067921798).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.10267615219883607).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 0.14688391368171685).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.5303948572093229).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -0.529363977329317).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -0.6623304931849363).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.6626231415845181).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.06783382350879162).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.36423142556823856).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.9730909692986618).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.8353557746972768).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.5361169534193021).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 0.6167735989645307).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.6122117071342573).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.5806373032413467).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.968052322606287).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.9245566150350051).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.6534917441628949).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.6715662235608231).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.7407238202696524).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 0.7354982992829906).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.06340668623729523).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.40591946498827336).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.4557556128718794).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.558559842127882).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.923796560084577).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.9557686157990668).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.6313087990584325).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.6299330011745).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.20274234705300925).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.21068723974704434).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.5124187849542257).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.3701684439747759).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.3038733131602001).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.2768594302675577).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.26284256852387516).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.3071432058996983).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.7502523839911145).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.719745733523908).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.868874517623681).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -0.5062300204223075).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 0.6874509025876478).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -0.6826684237245009).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.3757979651191995).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.3369000264078134).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 0.5165579149683887).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.9838406309684837).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.6517543596020707).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.8938908007211287).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 0.011576333256837757).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 0.1994965304792813).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.5357402786793479).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.5797224477448737).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.6015756389470484).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.573317645438219).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.3791786031325414).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.676931394322152).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * 0.6257613274555152).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -0.6210571332355261).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.45193657844083596).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 0.16633011275543763).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.8632357323678501).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.5580904452638696).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.7226189706701976).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.7708292466716248).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.628899885711077).on(cirq.GridQubit(5, 0)),
                cirq.Rz(np.pi * 0.8564821803203452).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.48600051750832335).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.40704671139578114).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.7509923227943213).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.7705635810307807).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.5247429096711106).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.31560248875795377).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.4445283033807374).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -0.43843587057450184).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.23079678484166474).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.24296757608244463).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.6933510795197081).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.7747059716945244).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.6297402023667946).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -0.650250406527777).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.8327738427573091).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.8966188475674683).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.12025352080627527).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -0.029370019547682955).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5508555127616375, phi=0.48773645023966805).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)
                ),
                cirq.FSimGate(theta=1.4860895179182787, phi=0.49800223593597315).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5268891182960795, phi=0.5146971591948788).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)
                ),
                cirq.FSimGate(theta=1.5004518396933153, phi=0.541239891546859).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5996085979256793, phi=0.5279139399675195).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)
                ),
                cirq.FSimGate(theta=1.5354845176224254, phi=0.41898979144044296).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)
                ),
                cirq.FSimGate(theta=1.545842827888829, phi=0.533679342490625).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5651524165810975, phi=0.5296573901163858).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.6240366191418867, phi=0.48516108212176406).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)
                ),
                cirq.FSimGate(theta=1.6022614099028112, phi=0.5001380228896306).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.574931196238987, phi=0.5236666378689078).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5238301684218176, phi=0.47521120348925566).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5426970250652188, phi=0.5200449092580564).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.4235475054732074, phi=0.5253841271266504).on(
                    cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.511471063363894, phi=0.4578807555552488).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5371762819242982, phi=0.5674318212304278).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.510414477168897, phi=0.44988262527024675).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.498535212903308, phi=0.637164678333888).on(
                    cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.507377591132129, phi=0.47869828403704195).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.48836082148729, phi=0.46458301209227065).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.5400981673597602, phi=0.5128416009465753).on(
                    cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.5860873970424136, phi=0.4790438939428006).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5630547528566316, phi=0.48589356877723594).on(
                    cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.6542790087648793).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -0.9830764940337477).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -0.7079366355498636).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 0.7127191144130105).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.5003181025167607).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.5392160412281468).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -0.4944938908636658).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.027211174863570817).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.5893795615335414).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.831516002652599).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -0.21350946680641048).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 0.42458233054252953).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.14729238052848453).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.19127454959401033).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.00982266418345571).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.018435329325373753).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.2092460914861244).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.08850669970348643).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -0.04816660891478307).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 0.05287080313477205).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.5144804279802232).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 0.2288739622948249).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.6539308607246773).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.9590761478286578).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.6105530873621177).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.5623428113606904).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.4541035216184288).on(cirq.GridQubit(5, 0)),
                cirq.Rz(np.pi * -0.22652122700916058).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.09920368129230818).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.020249875179765953).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.7703835607337791).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.7508123024973197).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.9299380908209051).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.8609214882659385).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.6603148238966917).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 0.6664072567029273).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.011997302735339959).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.02416809397611926).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.7541471791694208).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.6727922869946045).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.21828350563706272).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -0.2387937097980442).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.8775865857149596).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.9414315905251189).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.5077173122630191).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -0.4168338110044266).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.493850693839934).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.46824735745938767).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.2984751103100736).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -0.7975917880942631).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.2590669520927105).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.46553678230138035).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.4922863320894708).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.4386037696673656).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.9729214362671511).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.9612016987900408).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.4556017204511883).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.4602146990123172).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.17115863024938213).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.07406694571515549).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.04747985536414887).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.0015617338005978266).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.2389354663504067).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.2865947391710613).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.5880773071541381).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.6362285069775276).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.3964494752371541).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.38670528408761545).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.011734933093958058).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.0011415796799869179).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.5924971027747271).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.6771826672314938).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.42942159755003484).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.5342946187446849).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * -0.8039587731906531).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.6712120667598861).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.878510082642783).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.8658791452001359).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.13314967964918875).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.3134985834412089).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -0.13421982786758235).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.14142059663243078).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.24729161215179005).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.1789596367298805).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 0.7475635765288697).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * -0.8844707307377268).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.483304234663135, phi=0.4930986258758784).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5160176987076064, phi=0.49850252902921577).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.5338611249160479, phi=0.5011308712767845).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.480179689158691, phi=0.4772322221553844).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5152260103068818, phi=0.49796235787029736).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5284924549164072, phi=0.5160847019657471).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.58661284381037, phi=0.475779832809368).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5333295850816209, phi=0.44983388105304506).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5158107733607835, phi=0.4663776718737318).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5645151084457722, phi=0.47497942677256283).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.5659881784786247, phi=0.5656290235103623).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.5211879663086973, phi=0.5056110683638391).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5083349422212171, phi=0.49641600818144604).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5087002777200382, phi=0.44025777694304247).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5658333118222365, phi=0.47264531483343447).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5219378850865568, phi=0.5335829954491795).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.5501487671051402, phi=0.4404117539373896).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.4825325148661492, phi=0.6857341218223484).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.4941963673904604, phi=0.45895108234543025).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.5487430259667763, phi=0.4467898473637848).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.599747845729294).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.6253511821098403).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.9185238680705767).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.5823594541452338).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.017602831844571624).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.18886699836409832).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.4113331864284153).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.46501574885052055).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.7427018606296518).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.7309821231525422).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.4572604632711416).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.45264748471001387).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.8287439256872393).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.9260304983482223).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.5539049867836513).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.5048633976189045).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.17394491383358626).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.22160418665424148).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.24017847920109392).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.19202727937770428).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * -0.37039764324017677).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 0.38014183438971544).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.34101503555577156).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.35389154832971653).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.6559023537995501).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.5712167893427836).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.4498659567527707).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.34499293555812066).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.4151204811787974).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.5478671876095643).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.6044391967350843).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.5918082592924367).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.3382065832034761).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.5185554869954963).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 0.3976402333451519).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.3904394645803035).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.44626364529659257).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.8725148941782631).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * -0.7580489709662166).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * 0.6211418167573595).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.7988745176237023).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -0.43623002042232994).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 0.6854509025876576).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -0.6806684237245106).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.895797965119231).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.8569000264078449).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -0.5874420850315563).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.1201593690314567).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.1662456403979169).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.07589080072114174).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -0.7304236667431359).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 0.941496530479255).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.20225972132064465).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.15827755225511886).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.4344243610529689).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.46268235456179807).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.8068213968674496).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.509068605677839).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -0.48423867254446107).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 0.48894286676445003).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.15393657844081263).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.13166988724458512).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.9167642676321308).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.7780904452638893).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.9446189706702058).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.9928292466716331).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.5611001142888932).on(cirq.GridQubit(5, 0)),
                cirq.Rz(np.pi * -0.3335178196796271).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.9320005175083301).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.8530467113957879).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.43500767720566996).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.41543641896921035).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.7467429096710533).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.5376024887578965).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.2245283033807833).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -0.21843587057454775).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.5287967848416878).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.5409675760824668).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.6406489204802666).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.5592940283054504).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.2577402023668132).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -0.278250406527795).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.9067738427572684).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.9706188475674273).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.619746479193709).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 0.710629980452301).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5508555127616375, phi=0.48773645023966805).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)
                ),
                cirq.FSimGate(theta=1.4860895179182787, phi=0.49800223593597315).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5268891182960795, phi=0.5146971591948788).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)
                ),
                cirq.FSimGate(theta=1.5004518396933153, phi=0.541239891546859).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5996085979256793, phi=0.5279139399675195).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)
                ),
                cirq.FSimGate(theta=1.5354845176224254, phi=0.41898979144044296).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)
                ),
                cirq.FSimGate(theta=1.545842827888829, phi=0.533679342490625).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5651524165810975, phi=0.5296573901163858).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.6240366191418867, phi=0.48516108212176406).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)
                ),
                cirq.FSimGate(theta=1.6022614099028112, phi=0.5001380228896306).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.574931196238987, phi=0.5236666378689078).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5238301684218176, phi=0.47521120348925566).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5426970250652188, phi=0.5200449092580564).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.4235475054732074, phi=0.5253841271266504).on(
                    cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.511471063363894, phi=0.4578807555552488).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5371762819242982, phi=0.5674318212304278).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.510414477168897, phi=0.44988262527024675).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.498535212903308, phi=0.637164678333888).on(
                    cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.507377591132129, phi=0.47869828403704195).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.48836082148729, phi=0.46458301209227065).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.5400981673597602, phi=0.5128416009465753).on(
                    cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.5860873970424136, phi=0.4790438939428006).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5630547528566316, phi=0.48589356877723594).on(
                    cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.5842790087648996).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 0.9469235059662741).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -0.7059366355498733).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 0.7107191144130203).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.9796818974832071).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.9407839587718211).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 0.6095061091362723).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.9232111748636281).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.5926204384664704).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.35048399734741176).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 0.5284905331935638).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -0.3174176694574447).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.8852923805284783).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.929274549594004).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.9541773358165268).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.9824353293253562).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.9767539085138666).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.7254933002965229).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -0.9381666089148069).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 0.9428708031347959).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.8124804279802466).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 0.5268739622948487).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.8739308607246958).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.8209238521713237).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.8325530873621259).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.7843428113606987).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.7358964783815413).on(cirq.GridQubit(5, 0)),
                cirq.Rz(np.pi * 0.9634787729908084).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 0.34679631870769856).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.42575012482024077).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.41561643926621195).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.43518769750267156).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.8480619091791521).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.6389214882659956).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.4403148238967388).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 0.4464072567029743).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.28600269726468336).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.27383190602390434).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.579852820830554).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.6612077130053702).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.590283505637045).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -0.6107937097980273).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.8035865857150007).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.8674315905251597).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.7522826877369967).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 0.8431661889955893).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 0)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.6438506938399094).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.618247357459362).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.07047511031002901).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -0.5695917880942174).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.4070669520927599).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.6135367823014299).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.5682863320894853).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.5146037696673801).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.28907856373285357).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.30079830120996326).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.6756017204512074).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.6802146990123358).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.6911586302494148).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.44593305428487634).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 0.39452014463587903).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.44356173380062575).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.4290645336496083).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.38140526082895393).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.5160773071541702).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.564228506977561).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.6204494752371521).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.6107052840876123).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.9502650669060344).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.9631415796799797).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.8895028972252971).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.8048173327685305).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.6805784024500074).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.5757053812553574).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * -0.8799587731906682).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.7472120667599012).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.5825100826428156).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.5698791452001684).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.9028503203508277).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.7225014165588084).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 0.3857801721324489).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.3785794033676002).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.10329161215178768).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.3229596367298828).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 0.3035635765288527).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * -0.4404707307377103).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.483304234663135, phi=0.4930986258758784).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5160176987076064, phi=0.49850252902921577).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.5338611249160479, phi=0.5011308712767845).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.480179689158691, phi=0.4772322221553844).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5152260103068818, phi=0.49796235787029736).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5284924549164072, phi=0.5160847019657471).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.58661284381037, phi=0.475779832809368).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5333295850816209, phi=0.44983388105304506).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5158107733607835, phi=0.4663776718737318).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5645151084457722, phi=0.47497942677256283).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.5659881784786247, phi=0.5656290235103623).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.5211879663086973, phi=0.5056110683638391).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5083349422212171, phi=0.49641600818144604).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5087002777200382, phi=0.44025777694304247).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5658333118222365, phi=0.47264531483343447).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5219378850865568, phi=0.5335829954491795).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.5501487671051402, phi=0.4404117539373896).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.4825325148661492, phi=0.6857341218223484).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.4941963673904604, phi=0.45895108234543025).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.5487430259667763, phi=0.4467898473637848).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.7497478457292671).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.7753511821098146).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.8534761319293775).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.35435945414518916).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.16560283184462107).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.04086699836404887).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.4873331864284298).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.541015748850535).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.0047018606296570335).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.007017876847452668).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.6772604632711591).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.6726474847100307).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.6512560743127291).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.40603049834819016).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.9959049867836792).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.9468633976189325).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.8419449138336009).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.8896041866542553).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.16817847920112608).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.12002727937773534).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * -0.5943976432401735).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 0.6041418343897134).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.6209849644442211).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.6081084516702759).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.8260976462004742).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.9107832106572408).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.6601340432472717).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.7650070644419217).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.49112048117881246).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.6238671876095794).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.9004391967350515).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.8878082592924043).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.6257934167965067).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.4454445130044874).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -0.12235976665487905).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.12956053541972776).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.30226364529658795).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.7285148941782584).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * -0.31404897096620005).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * 0.17714181675734245).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.5516614516047799).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 0.6174795220715865).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.4327711187160072).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.05062333421393557).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.3177840441511373).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -0.10047261856343086).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.5094803678807461).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -0.477422600327394).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.6408765210346724).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.6213948502194439).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.7032192054252008).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 0.754622217740198).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.9073671101422918).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.7688260728280146).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.8617637363416806).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.9336663643285862).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.3929732311767222).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.4097429307239244).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.0552051208550207).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -0.04849439530424264).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.9954710267271799).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.9922667609489023).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.08109954594056305).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.03439016849657811).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.11890354904913102).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.06799568729138893).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.6030454946335517).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.5869432193241655).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * -0.9975512288793414).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.9798328527655973).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 0.676440254578787).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.9238318053231387).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.7743905036170879).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.8501311900075205).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.6828230291151024).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.7440183043132079).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -0.06546313715369771).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.05739220357069274).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -0.03844537611129621).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.037517804558631546).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.782361625590525).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.9364903862480225).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 0.7611409474788069).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.8031117186780351).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -0.38150923394940456).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.37485924771904144).on(cirq.GridQubit(8, 5)),
                cirq.Rz(np.pi * 0.03297060514310833).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * -0.3917017537983911).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5157741664069029, phi=0.5567125777723744).on(
                    cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5177580142209797, phi=0.4948108578225166).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.6036738621219824, phi=0.47689957001758815).on(
                    cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5177327089642791, phi=0.5058312223892585).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5253184444076096, phi=0.46557175536519374).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.6141004604574274, phi=0.494343440675308).on(
                    cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.5476810407275208, phi=0.44290174465702487).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5237261387830179, phi=0.4696616122846161).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5285844942020295, phi=0.5736654641906893).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5483159975149505, phi=0.4961408893973623).on(
                    cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.6377079485605028, phi=0.6888985951517526).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.529949914236052, phi=0.48258847574702635).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5280421758407217, phi=0.5109767145462891).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5120782868771674, phi=0.4815152809861558).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5071938854285831, phi=0.5089276063739265).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)
                ),
                cirq.FSimGate(theta=1.5460100224551203, phi=0.5302403303961576).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5166625940397171, phi=0.4517159790427676).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.4597689731864314, phi=0.4214985958536156).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.535649445690472, phi=0.47076284376181704).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)
                ),
                cirq.FSimGate(theta=1.5179778495708582, phi=0.5221350266177334).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.4969321270213238, phi=0.4326117171327162).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.5114987201637704, phi=0.4914319343687703).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)
                ),
                cirq.FSimGate(theta=1.4908807480930255, phi=0.4886243720131578).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)
                ),
                cirq.FSimGate(theta=1.616256999726831, phi=0.501428936283957).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.5641935842445645).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -0.4983755137777578).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.24179059583774581).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.7251850487676863).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.32084588367729194).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 0.5381573092649984).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.019062576518183987).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.01299519103516814).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.22619984017981742).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.2456815109950459).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.8617595478187416).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 0.9131625601337389).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.24317615795692585).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.38171719527120296).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.9034580610029361).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.9753606889898416).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.5871899251539519).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.603959624701154).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.29703548124351364).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * 0.3037462067942906).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * -0.20718859840113155).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.2103928641794091).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.18030203332281788).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.2270114107668028).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.04128661851581855).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.1456126178247014).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.8499898074110996).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.8660920827204859).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.26992216901673105).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.24730625066166856).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 0.4845073865505883).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.8842353266486614).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.8911052487304801).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.8153645623400477).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.0158265769954911).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.07702185219359665).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 0.5014707755967253).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.5095417091797303).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 0.3068636250628814).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.30779119661554605).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.5183942238917469).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.7995422120531994).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 0.9961315227572937).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.9618977060434781).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 0.26285448551587504).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.26950447174623815).on(cirq.GridQubit(8, 5)),
                cirq.Rz(np.pi * 0.6934649565591651).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * 0.947803894785552).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.08621640979886422).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 0.16334365608168644).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.3973572916277998).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -0.396326411747794).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.5427073576530422).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.5424147092534605).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.09003675765506945).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.34202849142196157).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.8983264693104055).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.7067732133063435).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.705156509293045).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -0.6244998637478164).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.15790347048791883).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.18947787438082972).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.8024559428448615).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.7589602352735803).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.8696926792305255).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.8516181998325968).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.8756084230940031).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -0.8808339440806644).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 0.24320434330005752).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.7125304945256264).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.9897343640361297).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.9074614067078688).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.9497630264840345).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.9177909707695425).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.12861597882367556).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.1299917767076041).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.13388452450572944).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.12593963181169407).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.9621689450218167).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.8955807139987333).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.7528365530460183).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.7258226701533779).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.7596124788130051).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.7153118414371823).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.6814566172688604).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.7119632677360634).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5192859850645715, phi=0.49387245572956845).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5120572609259932, phi=0.5211713721957417).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)
                ),
                cirq.FSimGate(theta=1.615096254724942, phi=0.7269644142795206).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5269188098932545, phi=0.5036266469194081).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5179602369002039, phi=0.4914328237769214).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.537427483096926, phi=0.45115204759967975).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.53486366638317, phi=0.46559889697604934).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5194586006330344, phi=0.5068560732280918).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5819908111894527, phi=0.5595875596558442).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.5070579127771144, phi=0.4520319437379419).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.527311970249325, phi=0.4920204543143157).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5139592614725292, phi=0.45916943035876673).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5425204049671604, phi=0.5057437054391503).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.5432564804093452, phi=0.5658780292653538).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.4611081680611278, phi=0.5435451345370095).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.4529959991143482, phi=0.43830813863531964).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.6239619425876082, phi=0.4985036227887135).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.4884560669186362, phi=0.4964777432807688).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5034760541420213, phi=0.5004774067921798).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.08867615219877248).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 0.16088391368177818).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.5836051427906996).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 0.5846360226707056).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.6636695068149479).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.6633768584153672).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.7278338235086499).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.2957685744316189).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.7470909692987385).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.9386442253028005).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.534116953419378).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 0.6147735989646066).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.057788292865813835).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.08936269675872473).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.9720523226063322).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.9285566150350509).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.24050825583717475).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.22243377643924597).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.968723820269696).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 0.9634982992830347).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.5154066862373383).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 0.04608053501176949).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.24375561287182076).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.3465598421278222).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.6402034399153681).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.608231384200875).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.4706912009416499).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.4720669988255795).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.1947423470531135).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.2026872397471489).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.518418784954393).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.37616844397494287).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.13212668683985648).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.15914056973249802).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.698842568523934).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.7431432058997568).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.3162523839911777).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.28574573352397464).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 0)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.9936614516048078).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -0.9405204779283867).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.37922888128394683).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.862623334213893).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.792215955848905).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -0.9904726185633891).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.6765196321192446).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.7085773996725973).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.4948765210346792).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.4753948502194507).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.40721920542516743).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 0.45862221774016465).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.019367110142323812).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.11917392717195331).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.04776373634167188).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.11966636432857744).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.6929732311767329).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.7097429307239397).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.9847948791450413).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * 0.9915056046958216).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.40547102672717017).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.40226676094889036).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.14290045405943544).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.1896098315034204).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.41690354904915433).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.23000431270863436).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.5270454946335372).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.510943219324151).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.48044877112063566).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.45783285276557767).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 0.08044025457880374).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.48016819467688143).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.9203905036170812).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.9961311900075136).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.12917697088491722).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.06798169568681166).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -0.5814631371537482).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.5733922035707443).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -0.6284453761113048).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.6275178045586413).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.7803616255905353).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.9384903862480122).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * -0.5008590525212017).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.45888828132197124).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 0.5784907660505968).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.5851407522809633).on(cirq.GridQubit(8, 5)),
                cirq.Rz(np.pi * 0.10497060514307784).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * -0.46370175379836065).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5157741664069029, phi=0.5567125777723744).on(
                    cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5177580142209797, phi=0.4948108578225166).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.6036738621219824, phi=0.47689957001758815).on(
                    cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5177327089642791, phi=0.5058312223892585).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5253184444076096, phi=0.46557175536519374).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.6141004604574274, phi=0.494343440675308).on(
                    cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.5476810407275208, phi=0.44290174465702487).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5237261387830179, phi=0.4696616122846161).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5285844942020295, phi=0.5736654641906893).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5483159975149505, phi=0.4961408893973623).on(
                    cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.6377079485605028, phi=0.6888985951517526).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.529949914236052, phi=0.48258847574702635).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5280421758407217, phi=0.5109767145462891).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5120782868771674, phi=0.4815152809861558).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5071938854285831, phi=0.5089276063739265).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)
                ),
                cirq.FSimGate(theta=1.5460100224551203, phi=0.5302403303961576).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5166625940397171, phi=0.4517159790427676).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.4597689731864314, phi=0.4214985958536156).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.535649445690472, phi=0.47076284376181704).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)
                ),
                cirq.FSimGate(theta=1.5179778495708582, phi=0.5221350266177334).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.4969321270213238, phi=0.4326117171327162).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.5114987201637704, phi=0.4914319343687703).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)
                ),
                cirq.FSimGate(theta=1.4908807480930255, phi=0.4886243720131578).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)
                ),
                cirq.FSimGate(theta=1.616256999726831, phi=0.501428936283957).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.9938064157554087).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -0.9403755137777857).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.5702094041622093).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.08681495123226317).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.789154116322751).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -0.571842690735044).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.7949374234818247).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.8269951910351775).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.08019984017982425).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.09968151099505272).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.8422404521812253).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -0.7908374398662281).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.6448238420430421).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.506282804728765).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 0.28254193899705515).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.21063931101014957).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.28718992515393654).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.30395962470114324).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.7429645187565517).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -0.7362537932057713).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.3828114015988804).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.3796071358206017).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.043697966677180636).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.0030114107668043153).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.25671338148420475).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.4436126178247247).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.7739898074110851).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.7900920827204714).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.7919221690167495).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.7693062506616914).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -0.919492613449433).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.5197646733513552).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.9628947512695266).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.9613645623400409).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.8278265769955084).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.889021852193614).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -0.9825292244032231).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.9744582908202193).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 0.8968636250628911).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.8977911966155546).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.5203942238917367).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.801542212053188).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 0.2581315227573).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.30010229395653043).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -0.6971455144841298).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.6904955282537633).on(cirq.GridQubit(8, 5)),
                cirq.Rz(np.pi * 0.6214649565591956).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * -0.9801961052144784).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.5757835902011161).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 0.8253436560816667).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.5646427083721929).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 0.5656735882521988).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.10070735765308102).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.10041470925350265).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.1299632423448818).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.5620284914219106).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.15632646931043123).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.03522678669363078).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.6288434907069298).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 0.7095001362521582).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.732096529512105).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.7005221256191941).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.13445594284484547).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.09096023527356352).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.5716926792305023).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.5536181998325734).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.9516084230940176).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -0.9568339440806789).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.27279565669992845).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.1965304945256404).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.3937343640361464).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.4965385932921524).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.2382369735159425).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.2702090292304356).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.905384021176354).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.9040082232924209).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.7978845245057673).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.7899396318117285).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.964168945021872).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.893580713998678).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.435163446953961).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.46217732984660476).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.4283875211869742).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.4726881585628004).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.7965433827311167).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.7660367322639136).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5192859850645715, phi=0.49387245572956845).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5120572609259932, phi=0.5211713721957417).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)
                ),
                cirq.FSimGate(theta=1.615096254724942, phi=0.7269644142795206).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5269188098932545, phi=0.5036266469194081).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5179602369002039, phi=0.4914328237769214).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.537427483096926, phi=0.45115204759967975).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.53486366638317, phi=0.46559889697604934).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5194586006330344, phi=0.5068560732280918).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5819908111894527, phi=0.5595875596558442).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.5070579127771144, phi=0.4520319437379419).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.527311970249325, phi=0.4920204543143157).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5139592614725292, phi=0.45916943035876673).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5425204049671604, phi=0.5057437054391503).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.5432564804093452, phi=0.5658780292653538).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.4611081680611278, phi=0.5435451345370095).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.4529959991143482, phi=0.43830813863531964).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.6239619425876082, phi=0.4985036227887135).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.4884560669186362, phi=0.4964777432807688).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5034760541420213, phi=0.5004774067921798).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.7506761521987528).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -0.5011160863182021).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.37839485720929306).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -0.3773639773292872).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -0.8943304931850955).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.894623141584675).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.9478338235086012).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.5157685744315735).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.005090969298765407).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.19664422530282744).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.7998830465805966).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -0.7192264010353682).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.9477882928658377).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.9793626967587485).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.359947677393651).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.403443384964933).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.5385082558371981).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.5204337764392692).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.9552761797302897).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -0.9605017007169508).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 0.0005933137626453817).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.46991946498821424).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.8397556128717996).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.9425598421278055).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.17179656008465377).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.20376861579914693).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.495308799058324).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.49393300117439093).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.858742347053148).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.8666872397471868).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.5204187849544483).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.37816844397499816).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.9441266868398739).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.9711405697325176).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.4891574314760486).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.44485679410022244).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.8382523839912006).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.8077457335239976).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 9)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.5888745176237674).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -0.22623002042239165).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 0.6794509025876863).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -0.6746684237245404).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.4557979651193263).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.41690002640794016).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 0.1005579149686249).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.56784063096872).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.6202456403978841).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.3781091992788255).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -0.956423666743059).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -0.8325034695208208).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.41625972132062794).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.3722775522551022).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.45757563894697817).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.4293176454381487).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.36482139686742276).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.0670686056778122).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * 0.1857613274556098).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -0.1810571332356208).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.7400634215592568).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 0.9743301127553455).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.25676426763207516).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.5619095547360591).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.38938102932976887).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.3411707533283418).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.13110011428881016).on(cirq.GridQubit(5, 0)),
                cirq.Rz(np.pi * 0.09648218032046488).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.2700005175083498).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.1910467113958076).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.006992322794356819).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.026563581030815846).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.5872570903291188).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.7963975112422756).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.43547169661907276).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 0.44156412942530826).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.5772032151582435).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.5650324239174633).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.6426489204801907).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.5612940283053744).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.8582597976331332).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 0.8377495934721519).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.8712261572428549).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.8073811524326956).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.8397464791936613).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 0.930629980452254).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5508555127616375, phi=0.48773645023966805).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)
                ),
                cirq.FSimGate(theta=1.4860895179182787, phi=0.49800223593597315).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5268891182960795, phi=0.5146971591948788).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)
                ),
                cirq.FSimGate(theta=1.5004518396933153, phi=0.541239891546859).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5996085979256793, phi=0.5279139399675195).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)
                ),
                cirq.FSimGate(theta=1.5354845176224254, phi=0.41898979144044296).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)
                ),
                cirq.FSimGate(theta=1.545842827888829, phi=0.533679342490625).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5651524165810975, phi=0.5296573901163858).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.6240366191418867, phi=0.48516108212176406).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)
                ),
                cirq.FSimGate(theta=1.6022614099028112, phi=0.5001380228896306).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.574931196238987, phi=0.5236666378689078).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5238301684218176, phi=0.47521120348925566).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5426970250652188, phi=0.5200449092580564).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.4235475054732074, phi=0.5253841271266504).on(
                    cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.511471063363894, phi=0.4578807555552488).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5371762819242982, phi=0.5674318212304278).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.510414477168897, phi=0.44988262527024675).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.498535212903308, phi=0.637164678333888).on(
                    cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.507377591132129, phi=0.47869828403704195).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.48836082148729, phi=0.46458301209227065).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.5400981673597602, phi=0.5128416009465753).on(
                    cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.5860873970424136, phi=0.4790438939428006).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5630547528566316, phi=0.48589356877723594).on(
                    cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.37427900876496123).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 0.7369235059663369).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -0.6999366355499054).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 0.7047191144130511).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.5803181025168881).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.6192160412282741).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -0.07849389086390429).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.38878882513619073).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.13862043846650543).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.1035160026525532).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 0.754490533193488).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -0.5434176694573679).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.9007076194715385).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.8567254504060127).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.15382266418352536).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.12556467067469587).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.5347539085138397).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.8325066997034515).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * 0.3918333910851223).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -0.3871291968651333).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.29351957201968526).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.579126037705083).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.46606913927525023).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.1609238521712663).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.5014469126378489).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.5496571886392757).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.3058964783814538).on(cirq.GridQubit(5, 0)),
                cirq.Rz(np.pi * 0.5334787729907289).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.3152036812922806).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.2362498751797384).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.026383560733814825).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.006812302497355796).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.18206190917932413).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.027078511733832647).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.2196851761031195).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -0.21359274329688396).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.8199973027352478).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.832168093976028).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.5818528208304781).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.6632077130052944).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.2937164943630092).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 0.27320629020202797).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.5815865857151237).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.6454315905252832).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.5322826877370442).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 0.6231661889956362).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.9061493061601683).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.9317526425407147).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.6135248896901003).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.11440821190591195).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.8510669520929084).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.9424632176984219).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.7962863320895299).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.7426037696674247).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.07507856373287025).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.08679830120998447).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.6643982795487398).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.6597853009876091).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.25115863024950946).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.005933054284972138).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.2794798553640372).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.230438266199295).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.4330645336496544).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.38540526082900006).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.30007730715426284).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.34822850697765584).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * -0.7075505247628513).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 0.7172947159123899).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.16373493309398734).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.15085842032004207).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.6644971027746309).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.7491826672313975).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.010578402450135117).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.09429461874451604).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.8920412268092872).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.9752120667599447).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.30548991735708686).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.318120854799734).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.010850320350880316).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.169498583441139).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -0.054219827867455876).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.06142059663230459).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.32870838784822615).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.7549596367298966).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 0.9715635765288021).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * 0.8915292692623403).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.483304234663135, phi=0.4930986258758784).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5160176987076064, phi=0.49850252902921577).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.5338611249160479, phi=0.5011308712767845).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.480179689158691, phi=0.4772322221553844).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5152260103068818, phi=0.49796235787029736).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5284924549164072, phi=0.5160847019657471).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.58661284381037, phi=0.475779832809368).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5333295850816209, phi=0.44983388105304506).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5158107733607835, phi=0.4663776718737318).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5645151084457722, phi=0.47497942677256283).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.5659881784786247, phi=0.5656290235103623).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.5211879663086973, phi=0.5056110683638391).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5083349422212171, phi=0.49641600818144604).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5087002777200382, phi=0.44025777694304247).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5658333118222365, phi=0.47264531483343447).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5219378850865568, phi=0.5335829954491795).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.5501487671051402, phi=0.4404117539373896).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.4825325148661492, phi=0.6857341218223484).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.4941963673904604, phi=0.45895108234543025).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.5487430259667763, phi=0.4467898473637848).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.8002521542708073).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.774648817890261).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.16947613192924818).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -0.3296405458549402).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.6096028318447693).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.40313300163609944).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.7153331864284722).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.7690157488505774).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.209298139370324).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.22101787684743823).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.6627395367287836).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.6673525152899142).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.9087439256873666).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.8460304983480961).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.32190498678375845).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.2728633976190163).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.8459449138336471).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.8936041866543014).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.04782152079877905).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.09597272062217206).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.7336023567598287).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.7238581656102899).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.49301503555580056).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.5058915483297458).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.7279023537994534).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.6432167893426869).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.009865956752601861).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.0950070644420493).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.7191204811788571).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.851867187609624).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.21156080326504628).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.22419174070769343).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.48220658320354487).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.6625554869955641).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 0.3176402333450257).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.310439464580177).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.1297363547034259).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.2965148941782446).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * -0.9820489709661495).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * 0.8451418167572918).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.5188745176237864).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -0.15623002042241071).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 0.6774509025876966).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -0.6726684237245518).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.9757979651193572).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.9369000264079712).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 0.9965579149686958).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.5361593690312092).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.5617543596021294).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.8038908007211836).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 0.30157633325696676).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -0.09050346952084656).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.8457402786793784).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.8897224477448996).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.5784243610530388).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.6066823545618683).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.44917860313258545).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.746931394322196).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -0.9242386725443664).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 0.9289428667643553).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.9619365784407211).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 0.6763301127553222).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.03676426763205716).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.34190955473604107).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.16738102932976004).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.11917075332833355).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.6788998857112175).on(cirq.GridQubit(5, 0)),
                cirq.Rz(np.pi * 0.9064821803204925).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.716000517508356).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.6370467113958149).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.820992322794365).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.8405635810308246).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.36525709032917614).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.5743975112423332).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.6554716966190274).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 0.6615641294252584).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.2792032151582201).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.26703242391743887).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.023351079519834027).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.10470597169464968).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.7697402023668831).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -0.7902504065278677).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.7972261572428959).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.7333811524327367).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.4202535208063547).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -0.32937001954776157).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5508555127616375, phi=0.48773645023966805).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(0, 6)
                ),
                cirq.FSimGate(theta=1.4860895179182787, phi=0.49800223593597315).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5268891182960795, phi=0.5146971591948788).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(1, 7)
                ),
                cirq.FSimGate(theta=1.5004518396933153, phi=0.541239891546859).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5996085979256793, phi=0.5279139399675195).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(2, 8)
                ),
                cirq.FSimGate(theta=1.5354845176224254, phi=0.41898979144044296).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(3, 3)
                ),
                cirq.FSimGate(theta=1.545842827888829, phi=0.533679342490625).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5651524165810975, phi=0.5296573901163858).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.6240366191418867, phi=0.48516108212176406).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(3, 9)
                ),
                cirq.FSimGate(theta=1.6022614099028112, phi=0.5001380228896306).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.574931196238987, phi=0.5236666378689078).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5238301684218176, phi=0.47521120348925566).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5426970250652188, phi=0.5200449092580564).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.4235475054732074, phi=0.5253841271266504).on(
                    cirq.GridQubit(5, 0), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.511471063363894, phi=0.4578807555552488).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5371762819242982, phi=0.5674318212304278).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.510414477168897, phi=0.44988262527024675).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.498535212903308, phi=0.637164678333888).on(
                    cirq.GridQubit(6, 1), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.507377591132129, phi=0.47869828403704195).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.48836082148729, phi=0.46458301209227065).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.5400981673597602, phi=0.5128416009465753).on(
                    cirq.GridQubit(7, 2), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.5860873970424136, phi=0.4790438939428006).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5630547528566316, phi=0.48589356877723594).on(
                    cirq.GridQubit(8, 3), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.30427900876498026).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 0.666923505966356).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -0.6979366355499168).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 0.7027191144130615).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.8996818974830809).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.8607839587716949).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -0.9744938908639662).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.5072111748638711).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.6793795615334856).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.9215160026525442).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -0.5035094668065377).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 0.714582330542658).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.16270761947154028).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.11872545040601902).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.8101773358164577).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.8384353293252871).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.2792460914861695).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.01850669970344215).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -0.49816660891490155).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 0.5028708031348905).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.004480427980338054).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.28112603770506084).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.24606913927523225).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.05907614782875167).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.2794469126378407).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.3276571886392672).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.5041035216185739).on(cirq.GridQubit(5, 0)),
                cirq.Rz(np.pi * -0.2765212270092988).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 0.1307963187077267).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.20975012482027006).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.8403835607338236).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.8208123024973651).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.039938090820618236).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.24907851173377474).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.4396851761030696).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -0.4335927432968386).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.5219973027352212).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.5341680939760024).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.08414717916954664).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.0027922869947304236).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.07828350563697334).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -0.0987937097979534).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.5075865857151647).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.5714315905253242).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.20771731226294082).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -0.11683381100434823).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 9)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.7561493061601958).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.781752642540741).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.8415248896901449).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.3424082119059566).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.9990669520929577).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.7944632176983725).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.8722863320895433).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.8186037696674426).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.6629214362671234).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.6512016987900138).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.4443982795487218).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.4397853009875912).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.7711586302495393).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.5259330542850031).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 0.16252014463598846).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.21156173380073065).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.8989354663503306).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.9465947391709849).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.22807730715429672).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.2762285069776852).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * -0.48355052476285504).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 0.4932947159123926).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.7982650669060048).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.8111415796799502).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.8175028972253934).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.7328173327686268).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.8794215975498231).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.9842946187444742).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.8160412268092694).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.9487879332400408).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.6014899173570537).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.6141208547997015).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.9531496796491027).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.866501416558878).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 0.4657801721325751).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.4585794033677264).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.4727083878482263).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.8989596367298968).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 0.527563576528785).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * -0.6644707307376426).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.483304234663135, phi=0.4930986258758784).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5160176987076064, phi=0.49850252902921577).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.5338611249160479, phi=0.5011308712767845).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.480179689158691, phi=0.4772322221553844).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5152260103068818, phi=0.49796235787029736).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.5284924549164072, phi=0.5160847019657471).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.58661284381037, phi=0.475779832809368).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5333295850816209, phi=0.44983388105304506).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5158107733607835, phi=0.4663776718737318).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5645151084457722, phi=0.47497942677256283).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.5659881784786247, phi=0.5656290235103623).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.5211879663086973, phi=0.5056110683638391).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5083349422212171, phi=0.49641600818144604).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5087002777200382, phi=0.44025777694304247).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5658333118222365, phi=0.47264531483343447).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5219378850865568, phi=0.5335829954491795).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.5501487671051402, phi=0.4404117539373896).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.4825325148661492, phi=0.6857341218223484).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.4941963673904604, phi=0.45895108234543025).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.5487430259667763, phi=0.4467898473637848).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(8, 5)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.6502521542708336).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.6246488178902884).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.05852386807079644).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -0.5576405458549848).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.7576028318448186).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.5511330016361488).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.79133318642849).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.8450157488505907).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.9472981393703223).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.9590178768474319).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.44273953672876565).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.4473525152898963).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.5712560743126024).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.32603049834806397).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.763904986783784).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.7148633976190419).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.4860550861663379).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.43839581334568356).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.11982152079874969).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.1679727206221382).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.5096023567598313).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.4998581656102937).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.46898496444419163).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.4561084516702464).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.7540976462005708).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.8387832106573374).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.8998659567525601).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.794992935557909).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.7951204811788705).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.9278671876096419).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.08443919673492117).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.07180825929227404).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.48179341679643817).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.3014445130044189).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -0.20235976665500524).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.20956053541985398).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.273736354703426).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.15251489417824454).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * -0.5380489709661325).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * 0.4011418167572748).on(cirq.GridQubit(8, 5)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 9)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 0)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.3196614516048859).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 0.38547952207169484).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.8152288812838089).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.7013766657862495).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.12221595584903099).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 0.33952738143673855).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.23451963211921778).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.2665773996725705).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.056876521034694004).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.03739485021947005).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.48078079457493167).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -0.4293777822599345).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.6446328898575795).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.7831739271718566).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * 0.39423626365835546).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.3223336356714499).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.40702676882322575).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.390257069276019).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.10479487914523171).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * 0.11150560469601203).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.6354710267271366).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.6322667609488568).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.8149004540594265).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.861609831503416).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.6890964509507758).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.8759956872912957).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.2990454946334938).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.2829432193241075).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.9144487711205713).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.8918328527655134).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 0.2924402545788629).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.6921681946769406).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.6416094963829359).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.5658688099925057).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.5651769708849738).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.5039816956868637).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -0.1294631371539041).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.12139220357089683).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -0.3984453761113394).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.39751780455867475).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.7743616255905674).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.9444903862479824).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * -0.28685905252121613).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.24488828132199017).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -0.5415092339493901).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.5348592477190326).on(cirq.GridQubit(8, 5)),
                cirq.Rz(np.pi * 0.3209706051429841).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * -0.6797017537982691).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5157741664069029, phi=0.5567125777723744).on(
                    cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5177580142209797, phi=0.4948108578225166).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.6036738621219824, phi=0.47689957001758815).on(
                    cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5177327089642791, phi=0.5058312223892585).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5253184444076096, phi=0.46557175536519374).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.6141004604574274, phi=0.494343440675308).on(
                    cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.5476810407275208, phi=0.44290174465702487).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5237261387830179, phi=0.4696616122846161).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5285844942020295, phi=0.5736654641906893).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5483159975149505, phi=0.4961408893973623).on(
                    cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.6377079485605028, phi=0.6888985951517526).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.529949914236052, phi=0.48258847574702635).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5280421758407217, phi=0.5109767145462891).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5120782868771674, phi=0.4815152809861558).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5071938854285831, phi=0.5089276063739265).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)
                ),
                cirq.FSimGate(theta=1.5460100224551203, phi=0.5302403303961576).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5166625940397171, phi=0.4517159790427676).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.4597689731864314, phi=0.4214985958536156).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.535649445690472, phi=0.47076284376181704).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)
                ),
                cirq.FSimGate(theta=1.5179778495708582, phi=0.5221350266177334).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.4969321270213238, phi=0.4326117171327162).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.5114987201637704, phi=0.4914319343687703).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)
                ),
                cirq.FSimGate(theta=1.4908807480930255, phi=0.4886243720131578).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)
                ),
                cirq.FSimGate(theta=1.616256999726831, phi=0.501428936283957).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.33219358424467277).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -0.2663755137778638).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.9937905958379286).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.5228149512321297).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.1191541163228786).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 0.09815730926482896).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.7630625765181485).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -0.7310048089647958).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.35780015982015645).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.3383184890049325).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.04575954781887384).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 0.09716256013387105).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.6911761579570534).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * -0.8297171952713306).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.15945806100297222).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.23136068898987777).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.6128100748461002).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.5960403752988935).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.13703548124325787).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * 0.14374620679403818).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.15281140159891393).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.1496071358206341).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.7156979666771761).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.6689885892331867).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.8492866185157253).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.6623873821752053).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.5459898074110394).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.5620920827204257).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.3579221690168138).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.3353062506617558).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * 0.8685073865505079).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.7317646733514145).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.5248947512695437).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.600635437659974).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.7361734230044396).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.6749781478063295).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * 0.5654707755969294).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.5735417091799366).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * 0.6668636250629246).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.6677911966155893).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.5263942238917069).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.8075422120531571).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 0.04413152275731896).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.08610229395654488).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 0.42285448551587074).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.4295044717462282).on(cirq.GridQubit(8, 5)),
                cirq.Rz(np.pi * 0.4054649565592893).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * -0.7641961052145744).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 7)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.5617835902010525).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 0.8113436560816032).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.5493572916278294).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -0.5483264117478236).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.7747073576531985).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.7744147092536157).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.7899632423447435).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.7779715085782299).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.06967353068949138).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.26122678669355454).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.6308434907068533).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 0.7115001362520819).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.5979034704878248).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.6294778743807357).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.13045594284479936).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.0869602352735174).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.3223073207695666).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.3403818001674931).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.8203915769059411).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 0.8151660559192776).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 0.17920434330011353).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.6485304945256825).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.6057343640362102).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.7085385932922116).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.19776302648411406).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.16579097076962546).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.007384021176433596).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.00600822329250055).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.7898845245058673).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.781939631811833).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.9701689450220378).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.8875807139985098).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.0008365530460956168).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.02617732984654818).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.007612478813077853).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.036688158562739326).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.7694566172689431).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.7999632677361507).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5192859850645715, phi=0.49387245572956845).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5120572609259932, phi=0.5211713721957417).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)
                ),
                cirq.FSimGate(theta=1.615096254724942, phi=0.7269644142795206).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5269188098932545, phi=0.5036266469194081).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5179602369002039, phi=0.4914328237769214).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.537427483096926, phi=0.45115204759967975).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.53486366638317, phi=0.46559889697604934).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5194586006330344, phi=0.5068560732280918).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5819908111894527, phi=0.5595875596558442).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.5070579127771144, phi=0.4520319437379419).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.527311970249325, phi=0.4920204543143157).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5139592614725292, phi=0.45916943035876673).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5425204049671604, phi=0.5057437054391503).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.5432564804093452, phi=0.5658780292653538).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.4611081680611278, phi=0.5435451345370095).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.4529959991143482, phi=0.43830813863531964).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.6239619425876082, phi=0.4985036227887135).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.4884560669186362, phi=0.4964777432807688).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5034760541420213, phi=0.5004774067921798).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.7366761521986892).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -0.4871160863181386).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.7356051427907281).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 0.7366360226707339).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.4316695068147915).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.4313768584152086).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.3921661764915394).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.8242314255685659).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.22090903070115833).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.029355774697097447).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.8018830465805213).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -0.7212264010352928).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.3822117071340921).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.3506373032411812).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.3559476773936038).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.39944338496488685).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.5674917441627332).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.5855662235606597).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.7272761797302438).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -0.7325017007169073).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.4514066862373966).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.017919464988172252).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.6277556128717449).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.7305598421277463).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.6077965600847104).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * -0.639768615799199).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.6066912009417557).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.6080669988256887).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.850742347053257).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.8586872397472913).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.5264187849546164).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.38416844397516403).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.6198733131600651).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.5928594302674213).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.053157431475987546).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.008856794100170371).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.40425238399126495).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.3737457335240574).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 9)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 6)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 2)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.761661451604916).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * 0.827479522071725).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.37277111871624163).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.11062333421370002).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.7677840441509273).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * -0.5504726185632197).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * 0.5794803678807904).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * -0.5474226003274377).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.0891234789653003).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.10860514978052427).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.7767807945749653).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * -0.7253777822599681).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.46736711014245313).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.328826072828176).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.7917637363416363).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.8636663643285419).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.107026768823215).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.09025706927600828).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.8552051208547063).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -0.848494395303926).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.04547102672712247).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.04226676094884716).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.9610995459405717).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.9143901684965867).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.3910964509507547).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * 0.5779956872912702).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.2230454946334759).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.20694321932409412).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.3924487711205484).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.36983285276549044).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -0.30355974542111586).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.09616819467696185).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.4956094963829416).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.4198688099925114).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.6228230291150043).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.6840183043131144).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -0.6454631371539489).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.6373922035709507).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -0.9884453761113445).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.9875178045586844).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.7723616255905777).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.9464903862479721).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * 0.4511409474787776).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.4931117186780035).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * 0.4184907660506158).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * -0.42514075228097326).on(cirq.GridQubit(8, 5)),
                cirq.Rz(np.pi * 0.39297060514295473).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * -0.7517017537982353).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5157741664069029, phi=0.5567125777723744).on(
                    cirq.GridQubit(0, 6), cirq.GridQubit(1, 6)
                ),
                cirq.FSimGate(theta=1.5177580142209797, phi=0.4948108578225166).on(
                    cirq.GridQubit(1, 5), cirq.GridQubit(2, 5)
                ),
                cirq.FSimGate(theta=1.6036738621219824, phi=0.47689957001758815).on(
                    cirq.GridQubit(1, 7), cirq.GridQubit(2, 7)
                ),
                cirq.FSimGate(theta=1.5177327089642791, phi=0.5058312223892585).on(
                    cirq.GridQubit(2, 4), cirq.GridQubit(3, 4)
                ),
                cirq.FSimGate(theta=1.5253184444076096, phi=0.46557175536519374).on(
                    cirq.GridQubit(2, 6), cirq.GridQubit(3, 6)
                ),
                cirq.FSimGate(theta=1.6141004604574274, phi=0.494343440675308).on(
                    cirq.GridQubit(2, 8), cirq.GridQubit(3, 8)
                ),
                cirq.FSimGate(theta=1.5476810407275208, phi=0.44290174465702487).on(
                    cirq.GridQubit(3, 3), cirq.GridQubit(4, 3)
                ),
                cirq.FSimGate(theta=1.5237261387830179, phi=0.4696616122846161).on(
                    cirq.GridQubit(3, 5), cirq.GridQubit(4, 5)
                ),
                cirq.FSimGate(theta=1.5285844942020295, phi=0.5736654641906893).on(
                    cirq.GridQubit(3, 7), cirq.GridQubit(4, 7)
                ),
                cirq.FSimGate(theta=1.5483159975149505, phi=0.4961408893973623).on(
                    cirq.GridQubit(3, 9), cirq.GridQubit(4, 9)
                ),
                cirq.FSimGate(theta=1.6377079485605028, phi=0.6888985951517526).on(
                    cirq.GridQubit(4, 2), cirq.GridQubit(5, 2)
                ),
                cirq.FSimGate(theta=1.529949914236052, phi=0.48258847574702635).on(
                    cirq.GridQubit(4, 4), cirq.GridQubit(5, 4)
                ),
                cirq.FSimGate(theta=1.5280421758407217, phi=0.5109767145462891).on(
                    cirq.GridQubit(4, 6), cirq.GridQubit(5, 6)
                ),
                cirq.FSimGate(theta=1.5120782868771674, phi=0.4815152809861558).on(
                    cirq.GridQubit(4, 8), cirq.GridQubit(5, 8)
                ),
                cirq.FSimGate(theta=1.5071938854285831, phi=0.5089276063739265).on(
                    cirq.GridQubit(5, 1), cirq.GridQubit(6, 1)
                ),
                cirq.FSimGate(theta=1.5460100224551203, phi=0.5302403303961576).on(
                    cirq.GridQubit(5, 3), cirq.GridQubit(6, 3)
                ),
                cirq.FSimGate(theta=1.5166625940397171, phi=0.4517159790427676).on(
                    cirq.GridQubit(5, 5), cirq.GridQubit(6, 5)
                ),
                cirq.FSimGate(theta=1.4597689731864314, phi=0.4214985958536156).on(
                    cirq.GridQubit(5, 7), cirq.GridQubit(6, 7)
                ),
                cirq.FSimGate(theta=1.535649445690472, phi=0.47076284376181704).on(
                    cirq.GridQubit(6, 2), cirq.GridQubit(7, 2)
                ),
                cirq.FSimGate(theta=1.5179778495708582, phi=0.5221350266177334).on(
                    cirq.GridQubit(6, 4), cirq.GridQubit(7, 4)
                ),
                cirq.FSimGate(theta=1.4969321270213238, phi=0.4326117171327162).on(
                    cirq.GridQubit(6, 6), cirq.GridQubit(7, 6)
                ),
                cirq.FSimGate(theta=1.5114987201637704, phi=0.4914319343687703).on(
                    cirq.GridQubit(7, 3), cirq.GridQubit(8, 3)
                ),
                cirq.FSimGate(theta=1.4908807480930255, phi=0.4886243720131578).on(
                    cirq.GridQubit(7, 5), cirq.GridQubit(8, 5)
                ),
                cirq.FSimGate(theta=1.616256999726831, phi=0.501428936283957).on(
                    cirq.GridQubit(8, 4), cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.774193584244703).on(cirq.GridQubit(0, 6)),
                cirq.Rz(np.pi * -0.708375513777894).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * 0.1817905958379791).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.6651850487679207).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.7708458836770796).on(cirq.GridQubit(1, 7)),
                cirq.Rz(np.pi * 0.9881573092647872).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.05093742348185972).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.08299519103521241).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.5038001598201507).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.4843184890049268).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.34175954781890744).on(cirq.GridQubit(2, 8)),
                cirq.Rz(np.pi * 0.39316256013390466).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * -0.1968238420429139).on(cirq.GridQubit(3, 3)),
                cirq.Rz(np.pi * 0.05828280472863678).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.9734580610029804).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.954639311010114).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.912810074846111).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * -0.8960403752989042).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.9029645187568041).on(cirq.GridQubit(3, 9)),
                cirq.Rz(np.pi * -0.8962537932060238).on(cirq.GridQubit(4, 9)),
                cirq.Rz(np.pi * 0.7428114015989191).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.7396071358206437).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.9396979666771735).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.8929885892331886).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.5512866185156997).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.36438738217518435).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * 0.469989807411026).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.48609208272040777).on(cirq.GridQubit(5, 8)),
                cirq.Rz(np.pi * 0.8799221690168367).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.8573062506617788).on(cirq.GridQubit(6, 1)),
                cirq.Rz(np.pi * -0.5354926134495134).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.13576467335143572).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.3788947512695494).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.4546354376599796).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.07582657699558236).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.13702185219369245).on(cirq.GridQubit(6, 7)),
                cirq.Rz(np.pi * -0.9185292244030168).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.9104582908200186).on(cirq.GridQubit(7, 2)),
                cirq.Rz(np.pi * -0.7431363749370657).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.7422088033844056).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * 0.5283942238916967).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.8095422120531468).on(cirq.GridQubit(7, 6)),
                cirq.Rz(np.pi * -0.6938684772426748).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.6518977060434488).on(cirq.GridQubit(8, 3)),
                cirq.Rz(np.pi * -0.5371455144841352).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.5304955282537777).on(cirq.GridQubit(8, 5)),
                cirq.Rz(np.pi * 0.33346495655932323).on(cirq.GridQubit(8, 4)),
                cirq.Rz(np.pi * -0.6921961052146037).on(cirq.GridQubit(9, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(0, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 7)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(2, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 8)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(3, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 2)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 7)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 9)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 0)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 1)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 8)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 4)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(6, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 2)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(7, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 5)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 6)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 4)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(9, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * 0.7762164097989717).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * -0.5266563439184256).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * -0.41264270837216277).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * 0.41367358825216866).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.3327073576532407).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.33241470925365335).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * 0.9900367576553064).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * -0.5579715085782754).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * -0.8116735306894645).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.9967732133064724).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.035156509293171996).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * 0.04550013625205651).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * -0.29209652951219905).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * 0.26052212561928817).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * -0.5375440571552134).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * 0.5810397647264999).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.6203073207695876).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.6383818001675187).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * -0.7443915769059233).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * 0.7391660559192642).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * -0.33679565669986794).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.13253049452570093).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * -0.009734364036231385).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * 0.11253859329223283).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * 0.9902369735158686).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.9777909707696428).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * -0.9586159788235369).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * 0.9599917767074699).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * -0.5461154754940948).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * 0.5540603681881291).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * -0.9721689450220954).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.8855807139984568).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * -0.812836553046113).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * 0.7858226701534692).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * -0.8196124788130952).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * 0.775311841437278).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.7085433827310339).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.6780367322638263).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.FSimGate(theta=1.5192859850645715, phi=0.49387245572956845).on(
                    cirq.GridQubit(0, 5), cirq.GridQubit(1, 5)
                ),
                cirq.FSimGate(theta=1.5120572609259932, phi=0.5211713721957417).on(
                    cirq.GridQubit(1, 4), cirq.GridQubit(2, 4)
                ),
                cirq.FSimGate(theta=1.615096254724942, phi=0.7269644142795206).on(
                    cirq.GridQubit(1, 6), cirq.GridQubit(2, 6)
                ),
                cirq.FSimGate(theta=1.5269188098932545, phi=0.5036266469194081).on(
                    cirq.GridQubit(2, 5), cirq.GridQubit(3, 5)
                ),
                cirq.FSimGate(theta=1.5179602369002039, phi=0.4914328237769214).on(
                    cirq.GridQubit(2, 7), cirq.GridQubit(3, 7)
                ),
                cirq.FSimGate(theta=1.537427483096926, phi=0.45115204759967975).on(
                    cirq.GridQubit(3, 2), cirq.GridQubit(4, 2)
                ),
                cirq.FSimGate(theta=1.53486366638317, phi=0.46559889697604934).on(
                    cirq.GridQubit(3, 4), cirq.GridQubit(4, 4)
                ),
                cirq.FSimGate(theta=1.5194586006330344, phi=0.5068560732280918).on(
                    cirq.GridQubit(3, 6), cirq.GridQubit(4, 6)
                ),
                cirq.FSimGate(theta=1.5819908111894527, phi=0.5595875596558442).on(
                    cirq.GridQubit(3, 8), cirq.GridQubit(4, 8)
                ),
                cirq.FSimGate(theta=1.5070579127771144, phi=0.4520319437379419).on(
                    cirq.GridQubit(4, 1), cirq.GridQubit(5, 1)
                ),
                cirq.FSimGate(theta=1.527311970249325, phi=0.4920204543143157).on(
                    cirq.GridQubit(4, 3), cirq.GridQubit(5, 3)
                ),
                cirq.FSimGate(theta=1.5139592614725292, phi=0.45916943035876673).on(
                    cirq.GridQubit(4, 5), cirq.GridQubit(5, 5)
                ),
                cirq.FSimGate(theta=1.5425204049671604, phi=0.5057437054391503).on(
                    cirq.GridQubit(4, 7), cirq.GridQubit(5, 7)
                ),
                cirq.FSimGate(theta=1.5432564804093452, phi=0.5658780292653538).on(
                    cirq.GridQubit(5, 2), cirq.GridQubit(6, 2)
                ),
                cirq.FSimGate(theta=1.4611081680611278, phi=0.5435451345370095).on(
                    cirq.GridQubit(5, 4), cirq.GridQubit(6, 4)
                ),
                cirq.FSimGate(theta=1.4529959991143482, phi=0.43830813863531964).on(
                    cirq.GridQubit(5, 6), cirq.GridQubit(6, 6)
                ),
                cirq.FSimGate(theta=1.6239619425876082, phi=0.4985036227887135).on(
                    cirq.GridQubit(6, 3), cirq.GridQubit(7, 3)
                ),
                cirq.FSimGate(theta=1.4884560669186362, phi=0.4964777432807688).on(
                    cirq.GridQubit(6, 5), cirq.GridQubit(7, 5)
                ),
                cirq.FSimGate(theta=1.5034760541420213, phi=0.5004774067921798).on(
                    cirq.GridQubit(7, 4), cirq.GridQubit(8, 4)
                ),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.Rz(np.pi * -0.6013238478013305).on(cirq.GridQubit(0, 5)),
                cirq.Rz(np.pi * 0.8508839136818767).on(cirq.GridQubit(1, 5)),
                cirq.Rz(np.pi * 0.22639485720926408).on(cirq.GridQubit(1, 4)),
                cirq.Rz(np.pi * -0.22536397732925822).on(cirq.GridQubit(2, 4)),
                cirq.Rz(np.pi * 0.8736695068147584).on(cirq.GridQubit(1, 6)),
                cirq.Rz(np.pi * -0.873376858415171).on(cirq.GridQubit(2, 6)),
                cirq.Rz(np.pi * -0.17216617649158472).on(cirq.GridQubit(2, 5)),
                cirq.Rz(np.pi * 0.6042314255686158).on(cirq.GridQubit(3, 5)),
                cirq.Rz(np.pi * 0.9629090307011337).on(cirq.GridQubit(2, 7)),
                cirq.Rz(np.pi * -0.7713557746970705).on(cirq.GridQubit(3, 7)),
                cirq.Rz(np.pi * 0.13588304658049602).on(cirq.GridQubit(3, 2)),
                cirq.Rz(np.pi * -0.05522640103526752).on(cirq.GridQubit(4, 2)),
                cirq.Rz(np.pi * 0.5077882928659317).on(cirq.GridQubit(3, 4)),
                cirq.Rz(np.pi * -0.5393626967588426).on(cirq.GridQubit(4, 4)),
                cirq.Rz(np.pi * 0.31205232260641236).on(cirq.GridQubit(3, 6)),
                cirq.Rz(np.pi * -0.26855661503512585).on(cirq.GridQubit(4, 6)),
                cirq.Rz(np.pi * -0.2694917441627076).on(cirq.GridQubit(3, 8)),
                cirq.Rz(np.pi * 0.2875662235606386).on(cirq.GridQubit(4, 8)),
                cirq.Rz(np.pi * 0.6512761797302304).on(cirq.GridQubit(4, 1)),
                cirq.Rz(np.pi * -0.6565017007168895).on(cirq.GridQubit(5, 1)),
                cirq.Rz(np.pi * 0.06459331376258938).on(cirq.GridQubit(4, 3)),
                cirq.Rz(np.pi * -0.5339194649881582).on(cirq.GridQubit(5, 3)),
                cirq.Rz(np.pi * 0.7762443871282764).on(cirq.GridQubit(4, 5)),
                cirq.Rz(np.pi * -0.673440157872275).on(cirq.GridQubit(5, 5)),
                cirq.Rz(np.pi * -0.5802034399152723).on(cirq.GridQubit(4, 7)),
                cirq.Rz(np.pi * 0.5482313842007837).on(cirq.GridQubit(5, 7)),
                cirq.Rz(np.pi * 0.35930879905821483).on(cirq.GridQubit(5, 2)),
                cirq.Rz(np.pi * -0.3579330011742818).on(cirq.GridQubit(6, 2)),
                cirq.Rz(np.pi * 0.4852576529467051).on(cirq.GridQubit(5, 4)),
                cirq.Rz(np.pi * -0.47731276025267083).on(cirq.GridQubit(6, 4)),
                cirq.Rz(np.pi * 0.5284187849546694).on(cirq.GridQubit(5, 6)),
                cirq.Rz(np.pi * -0.38616844397522154).on(cirq.GridQubit(6, 6)),
                cirq.Rz(np.pi * 0.19212668683995227).on(cirq.GridQubit(6, 3)),
                cirq.Rz(np.pi * -0.21914056973259607).on(cirq.GridQubit(7, 3)),
                cirq.Rz(np.pi * 0.7588425685240298).on(cirq.GridQubit(6, 5)),
                cirq.Rz(np.pi * -0.803143205899847).on(cirq.GridQubit(7, 5)),
                cirq.Rz(np.pi * 0.926252383991288).on(cirq.GridQubit(7, 4)),
                cirq.Rz(np.pi * -0.8957457335240803).on(cirq.GridQubit(8, 4)),
            ]
        ),
        cirq.Moment(
            operations=[
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(0, 5)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(0, 6)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(1, 4)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(1, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(1, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(2, 6)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(2, 8)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 2)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 3)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 4)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(3, 5)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 7)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 8)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(3, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 1)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 3)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(4, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(4, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(4, 9)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 0)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 3)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(5, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 5)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 6)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(5, 7)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(5, 8)
                ),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 1)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 2)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 3)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 4)),
                (cirq.X ** 0.5).on(cirq.GridQubit(6, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(6, 7)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 2)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 3)
                ),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(7, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 5)),
                (cirq.X ** 0.5).on(cirq.GridQubit(7, 6)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(8, 3)),
                cirq.PhasedXPowGate(phase_exponent=0.25, exponent=0.5).on(
                    cirq.GridQubit(8, 4)
                ),
                (cirq.X ** 0.5).on(cirq.GridQubit(8, 5)),
                (cirq.Y ** 0.5).on(cirq.GridQubit(9, 4)),
            ]
        ),
    ]
)

