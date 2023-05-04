from models import Creature
from images import *

# CAMBRIAN PERIOD CREATURES #
p1c1 = Creature()
p1c2 = Creature()
p1c3 = Creature()
p1c4 = Creature()
p1c5 = Creature()

p1c1.add_image(redlichia_img)
p1c1.id = 0
p1c1.genus = 'Genus: Redlichia'
p1c1.family = 'Family: Redlichiidae'
p1c1.order = 'Order: Redlichiida'
p1c1.class_ = 'Class: Trilobita'
p1c1.phylum = 'Phylum: Arthropoda'
p1c1.prestige = 'Prestige: * / ***'
p1c1.min_length = 0.60
p1c1.max_length_increment = 80
p1c1.min_weight = 1.6
p1c1.max_weight_increment = 40
p1c1.description = 'Large to very large species of trilobite found in the Lower to Middle Cambrian. '
p1c1.description += 'These trilobites were deposit feeders and lived on the ocean floor. '
p1c1.description += 'One distinct species, Redlichia Rex, was especially large, carnivorous, and potentially cannibalistic.'
p1c1.rarity = 0

p1c2.add_image(peytoia_img)
p1c2.id = 1
p1c2.genus = 'Genus: Peytoia'
p1c2.family = 'Family: Hurdiidae'
p1c2.order = 'Order: Radiodonta'
p1c2.class_ = 'Class: Dinocaridida'
p1c2.phylum = 'Phylum: Arthropoda'
p1c2.prestige = 'Prestige: * / ***'
p1c2.min_length = 0.60
p1c2.max_length_increment = 60
p1c2.min_weight = 7
p1c2.max_weight_increment = 400
p1c2.description = 'Peytoia was a genus of an early diverging order of stem-group arthropods. '
p1c2.description += 'These creatures were fast-moving carnivores that had two frontal appendages with long spines. '
p1c2.description += 'It was first believed that the Peytoia used their frontal appendages to sift through sediment for food; '
p1c2.description += 'although, it was later determined that a more logical explanation would be that the Peytoia '
p1c2.description += 'was a predator and used their frontal appendages to capture slow-moving prey. '
p1c2.rarity = 0

p1c3.add_image(titanokorys_img)
p1c3.id = 2
p1c3.genus = 'Genus: Titanokorys'
p1c3.family = 'Family: Hurdiidae'
p1c3.order = 'Order: Radiodonta'
p1c3.class_ = 'Class: Dinocaridida'
p1c3.phylum = 'Phylum: Arthropoda'
p1c3.prestige = 'Prestige: ** / ***'
p1c3.min_length = 1
p1c3.max_length_increment = 75
p1c3.min_weight = 30
p1c3.max_weight_increment = 1000
p1c3.description = 'This animal was the largest member of the Hurdiidae family and one of the largest animals of the Cambrian Period. '
p1c3.description += 'Titanokorys\' were primarily found in the Middle Cambrian and sifted through sand on the ocean floor to find prey. '
p1c3.description += 'It bears similar resemblance to another genus of the Hurdiidae family: the Cambroraster.'
p1c3.rarity = 1

p1c4.add_image(paradoxide_img)
p1c4.id = 3
p1c4.genus = 'Genus: Paradoxide'
p1c4.family = 'Family: Paradoxididae'
p1c4.order = 'Order: Redlichiida'
p1c4.class_ = 'Class: Trilobita'
p1c4.phylum = 'Phylum: Arthropoda'
p1c4.prestige = 'Prestige: ** / ***'
p1c4.min_length = 1
p1c4.max_length_increment = 50
p1c4.min_weight = 50
p1c4.max_weight_increment = 800
p1c4.description = 'Large to very large species of trilobite found all over the world during the Middle Cambrian. '
p1c4.rarity = 1

p1c5.add_image(anomalocaris_img)
p1c5.id = 4
p1c5.genus = 'Genus: Anomalocaris \'abnormal shrimp\''
p1c5.family = 'Family: Anomalocarididae'
p1c5.order = 'Order: Radiodonta'
p1c5.class_ = 'Class: Dinocaridida'
p1c5.phylum = 'Phylum: Arthropoda'
p1c5.prestige = 'Prestige: *** / ***'
p1c5.min_length = 0.80
p1c5.max_length_increment = 45
p1c5.min_weight = 12
p1c5.max_weight_increment = 400
p1c5.description = 'The first apex predator ever to exist. Anomalocaris dominated the Cambrian seas and '
p1c5.description += 'preyed on hard-bodied animals such as trilobites. '
p1c5.description += 'Their body structure included a row of swimming flaps on either side, large compound eyes, and two frontal appendages.'
p1c5.rarity = 2

# ORDOVICIAN PERIOD CREATURES #
p2c1 = Creature()
p2c2 = Creature()
p2c3 = Creature()
p2c4 = Creature()
p2c5 = Creature()

p2c1.add_image(arandaspis_img)
p2c1.id = 5
p2c1.genus = 'Genus: Arandaspis'
p2c1.family = 'Family: Arandaspididae'
p2c1.order = 'Order: Arandaspidida'
p2c1.class_ = 'Class: Pteraspidomorphi'
p2c1.phylum = 'Phylum: Chordata'
p2c1.prestige = 'Prestige: * / ***'
p2c1.min_length = 0.42
p2c1.max_length_increment = 21
p2c1.min_weight = 1.3
p2c1.max_weight_increment = 60
p2c1.description = 'Jawless fish from the Ordovician Period. '
p2c1.description += 'With no fins present, this fish used its flat tail to propel itself, similar to the movement of a tadpole.'
p2c1.rarity = 0

p2c2.add_image(aphetoceras_img)
p2c2.id = 6
p2c2.genus = 'Genus: Aphetoceras'
p2c2.family = 'Family: Estonioceratidae'
p2c2.order = 'Order: Tarphycerida'
p2c2.class_ = 'Class: Cephalopoda'
p2c2.phylum = 'Phylum: Mollusca'
p2c2.prestige = 'Prestige: * / ***'
p2c2.min_length = 0.80
p2c2.max_length_increment = 40
p2c2.min_weight = 2
p2c2.max_weight_increment = 140
p2c2.description = 'Cephalopod of the Lower Ordovician.'
p2c2.rarity = 0

p2c3.add_image(isoletus_img)
p2c3.id = 7
p2c3.genus = 'Genus: Isotelus'
p2c3.family = 'Family: Asaphidae'
p2c3.order = 'Order: Asaphida'
p2c3.class_ = 'Class: Trilobita'
p2c3.phylum = 'Phylum: Arthropoda'
p2c3.prestige = 'Prestige: ** / ***'
p2c3.min_length = 1
p2c3.max_length_increment = 30
p2c3.min_weight = 8
p2c3.max_weight_increment = 100
p2c3.description = 'Species of trilobite from the Middle to Upper Ordovician. '
p2c3.description += 'Includes a species (Isoletus rex) that currently holds the world record '
p2c3.description += 'for the largest complete trilobite fossil ever found. '
p2c3.rarity = 1

p2c4.add_image(megalograptus_img)
p2c4.id = 8
p2c4.genus = 'Genus: Megalograptus'
p2c4.family = 'Family: Megalograptidae'
p2c4.order = 'Order: Eurypterida'
p2c4.class_ = 'Class: [ ? ]'
p2c4.phylum = 'Phylum: Arthropoda'
p2c4.prestige = 'Prestige: ** / ***'
p2c4.min_length = 1.8
p2c4.max_length_increment = 120
p2c4.min_weight = 6
p2c4.max_weight_increment = 400
p2c4.description = 'Species of large predatory eurypterids that lived close to the shore. '
p2c4.rarity = 1

p2c5.add_image(aegirocassis_img)
p2c5.id = 9
p2c5.genus = 'Genus: Aegirocassis'
p2c5.family = 'Family: Hurdiidae'
p2c5.order = 'Order: Radiodonta'
p2c5.class_ = 'Class: Dinocaridida'
p2c5.phylum = 'Phylum: Arthropoda'
p2c5.prestige = 'Prestige: *** / ***'
p2c5.min_length = 6
p2c5.max_length_increment = 200
p2c5.min_weight = 150
p2c5.max_weight_increment = 10000
p2c5.description = 'Species of giant filter-feeder from the Lower Ordovician. '
p2c5.rarity = 2

# SILURIAN PERIOD CREATURES #
p3c1 = Creature()
p3c2 = Creature()
p3c3 = Creature()
p3c4 = Creature()
p3c5 = Creature()

p3c1.add_image(birkenia_img)
p3c1.id = 10
p3c1.genus = 'Genus: Birkenia'
p3c1.family = 'Family: Birkeniidae'
p3c1.order = 'Order: Birkeniiformes'
p3c1.class_ = 'Class: Anaspida'
p3c1.phylum = 'Phylum: 	Chordata'
p3c1.prestige = 'Prestige: * / ***'
p3c1.min_length = 0.3
p3c1.max_length_increment = 40
p3c1.min_weight = 0.6
p3c1.max_weight_increment = 60
p3c1.description = 'Jawless fish from the Middle Silurian.'
p3c1.rarity = 0

p3c2.add_image(poraspis_img)
p3c2.id = 11
p3c2.genus = 'Genus: Poraspis'
p3c2.family = 'Family: Cyathaspidae'
p3c2.order = 'Order: Cyathaspidiformes'
p3c2.class_ = 'Class: Pteraspidomorphi'
p3c2.phylum = 'Phylum: Chordata'
p3c2.prestige = 'Prestige: * / ***'
p3c2.min_length = 0.4
p3c2.max_length_increment = 40
p3c2.min_weight = 0.7
p3c2.max_weight_increment = 70
p3c2.description = 'Jawless fish from the the Late Silurian. '
p3c2.description += 'This fish was covered in plates and scales that provided protection. '
p3c2.description += 'These species resembled armored tadpoles. '
p3c2.rarity = 0

p3c3.add_image(entelognathus_img)
p3c3.id = 12
p3c3.genus = 'Genus: Entelognathus'
p3c3.family = 'Family: [ ? ]'
p3c3.order = 'Order: [ ? ]'
p3c3.class_ = 'Class: Placodermi'
p3c3.phylum = 'Phylum: Chordata'
p3c3.prestige = 'Prestige: ** / ***'
p3c3.min_length = 0.7
p3c3.max_length_increment = 50
p3c3.min_weight = 2.2
p3c3.max_weight_increment = 440
p3c3.description = 'Earlier species of armored and jawed-fish from the Late Silurian. '
p3c3.rarity = 1

p3c4.add_image(sphoocheras_img)
p3c4.id = 13
p3c4.genus = 'Genus: Sphooceras'
p3c4.family = 'Family: Sphooceratidae'
p3c4.order = 'Order: Orthocerida'
p3c4.class_ = 'Class: Cephalopoda'
p3c4.phylum = 'Phylum: Mollusca'
p3c4.prestige = 'Prestige: ** / ***'
p3c4.min_length = 0.75
p3c4.max_length_increment = 25
p3c4.min_weight = 1.5
p3c4.max_weight_increment = 100
p3c4.description = 'Species of primitive cephalopod from the Silurian Period. '
p3c4.description += 'Among the earliest cephalopods to have a fully-covered mantle.'
p3c4.rarity = 1

p3c5.add_image(megamastax_img)
p3c5.id = 14
p3c5.genus = 'Genus: Megamastax \'big mouth\''
p3c5.family = 'Family: [ ? ]'
p3c5.order = 'Order: [ ? ]'
p3c5.class_ = 'Class: [ ? ]'
p3c5.phylum = 'Phylum: Chordata'
p3c5.prestige = 'Prestige: *** / ***'
p3c5.min_length = 2.8
p3c5.max_length_increment = 120
p3c5.min_weight = 28
p3c5.max_weight_increment = 400
p3c5.description = 'Species of lobe-finned fish from the Late Silurian. '
p3c5.description += 'Due to its large size and predatory lifestyle, the Megamastax is believed to be the first vertebrate apex predator.'
p3c5.rarity = 2

# DEVONIAN PERIOD CREATURES #
p4c1 = Creature()
p4c2 = Creature()
p4c3 = Creature()
p4c4 = Creature()
p4c5 = Creature()

p4c1.add_image(bothriolepis_img)
p4c1.id = 15
p4c1.genus = 'Genus: Bothriolepis'
p4c1.family = 'Family: Bothriolepididae'
p4c1.order = 'Order: Antiarchi'
p4c1.class_ = 'Class: Placodermi'
p4c1.phylum = 'Phylum: Chordata'
p4c1.prestige = 'Prestige: * / ***'
p4c1.min_length = 1
p4c1.max_length_increment = 100
p4c1.min_weight = 10
p4c1.max_weight_increment = 1000
p4c1.description = 'Abundant and diverse genus of antiarch placoderms from the Middle to Late Devonian. They were widespread around the globe and found in near shore freshwater areas.'
p4c1.rarity = 0

p4c2.add_image(cladoselache_img)
p4c2.id = 16
p4c2.genus = 'Genus: Cladoselache'
p4c2.family = 'Family: Cladoselachidae'
p4c2.order = 'Order: Symmoriiformes'
p4c2.class_ = 'Class: Chondrichthyes'
p4c2.phylum = 'Phylum: Chordata'
p4c2.prestige = 'Prestige: * / ***'
p4c2.min_length = 3
p4c2.max_length_increment = 200
p4c2.min_weight = 60
p4c2.max_weight_increment = 4000
p4c2.description = 'Cartilaginous shark-like fish from the Late Devonian. It had a similar body shape to that of the modern day Great White Shark, although not related. The Cladoselache were believed to be fast-moving and agile predators.'
p4c2.rarity = 0

p4c3.add_image(gemuendina_img)
p4c3.id = 17
p4c3.genus = 'Genus: Gemuendina'
p4c3.family = 'Family: Asterosteidae'
p4c3.order = 'Order: Rhenanida'
p4c3.class_ = 'Class: Placodermi'
p4c3.phylum = 'Phylum: Chordata'
p4c3.prestige = 'Prestige: ** / ***'
p4c3.min_length = 1
p4c3.max_length_increment = 100
p4c3.min_weight = 3
p4c3.max_weight_increment = 200
p4c3.description = 'A placoderm from the Early Devonian with a body shape resembling that of a ray.'
p4c3.rarity = 1

p4c4.add_image(xenacanthus_img)
p4c4.id = 18
p4c4.genus = 'Genus: Xenacanthus'
p4c4.family = 'Family: Xenacanthidae'
p4c4.order = 'Order: Xenacanthida'
p4c4.class_ = 'Class: Chondrichthyes'
p4c4.phylum = 'Phylum: Chordata'
p4c4.prestige = 'Prestige: ** / ***'
p4c4.min_length = 3
p4c4.max_length_increment = 300
p4c4.min_weight = 80
p4c4.max_weight_increment = 4000
p4c4.description = 'Widespread genus of prehistoric freshwater shark that lived from the Late Devonian through the Triassic (post-Paleozoic Era). A distinct spine projected from the back of its head. It is believed that the spine may have been venomous.'
p4c4.rarity = 1

p4c5.add_image(onychodus_img)
p4c5.id = 19
p4c5.genus = 'Genus: Onychodus'
p4c5.family = 'Family: Onychodontidae'
p4c5.order = 'Order: Onychodontida'
p4c5.class_ = 'Class: Sarcopterygii'
p4c5.phylum = 'Phylum: Chordata'
p4c5.prestige = 'Prestige: *** / ***'
p4c5.min_length = 6
p4c5.max_length_increment = 200
p4c5.min_weight = 140
p4c5.max_weight_increment = 6000
p4c5.description = 'Lobe-finned fish from the Devonian. One of the best known onychodontiformes.'
p4c5.rarity = 2

# CARBONIFEROUS PERIOD CREATURES #
p5c1 = Creature()
p5c2 = Creature()
p5c3 = Creature()
p5c4 = Creature()
p5c5 = Creature()

p5c1.add_image(tristychius_img)
p5c1.id = 20
p5c1.genus = 'Genus: Tristychius'
p5c1.family = 'Family: Tristychiidae'
p5c1.order = 'Order: Hybodontiformes'
p5c1.class_ = 'Class: Chondrichthyes'
p5c1.phylum = 'Phylum: Chordata'
p5c1.prestige = 'Prestige: * / ***'
p5c1.min_length = 3
p5c1.max_length_increment = 100
p5c1.min_weight = 30
p5c1.max_weight_increment = 1000
p5c1.description = 'A small shark from the Carboniferous with an appearance resembling that of a modern dogfish. Tristychius also had spikes attached to the base of their dorsal fins, likely to ward off predators.'
p5c1.rarity = 0

p5c2.add_image(dracopristis_img)
p5c2.id = 21
p5c2.genus = 'Genus: Dracopristis'
p5c2.family = 'Family: [ ? ]'
p5c2.order = 'Order: Ctenacanthiformes'
p5c2.class_ = 'Class: Chondrichthyes'
p5c2.phylum = 'Phylum: Chordata'
p5c2.prestige = 'Prestige: * / ***'
p5c2.min_length = 6
p5c2.max_length_increment = 200
p5c2.min_weight = 140
p5c2.max_weight_increment = 6000
p5c2.description = 'Shark-like fish featuring 12 rows of teeth and an array of spines on its dorsal fins. Dracopristis had larger but less flexible jaws than that of the modern shark.'
p5c2.rarity = 0

p5c3.add_image(rhizodus_img)
p5c3.id = 22
p5c3.genus = 'Genus: Rhizodus'
p5c3.family = 'Family: Rhizodontidae'
p5c3.order = 'Order: Rhizodontiformes'
p5c3.class_ = 'Class: Rhizodontida'
p5c3.phylum = 'Phylum: Chordata'
p5c3.prestige = 'Prestige: ** / ***'
p5c3.min_length = 12
p5c3.max_length_increment = 300
p5c3.min_weight = 300
p5c3.max_weight_increment = 10000
p5c3.description = 'This giant rhizodont had two 8 inch fangs in the front of their jaws. The Rhizodus was an enormous apex predator tpyically found in large river systems and swamps. It fed on amphibians and other smaller marine animals.'
p5c3.rarity = 1

p5c4.add_image(orthacanthus_img)
p5c4.id = 23
p5c4.genus = 'Genus: Orthacanthus'
p5c4.family = 'Family: Orthacanthidae'
p5c4.order = 'Order: Xenacanthida'
p5c4.class_ = 'Class: Chondrichthyes'
p5c4.phylum = 'Phylum: Chordata'
p5c4.prestige = 'Prestige: ** / ***'
p5c4.min_length = 8
p5c4.max_length_increment = 200
p5c4.min_weight = 200
p5c4.max_weight_increment = 10000
p5c4.description = 'Freshwater xenacanthid shark with an occasionally cannibalistic diet. The Orthocanthus was the apex predator of freshwater swamps and bayous. (one of my favorites)' 
p5c4.rarity = 1

p5c5.add_image(diplocaulus_img)
p5c5.id = 24
p5c5.genus = 'Genus: Diplocaulus'
p5c5.family = 'Family: Diplocaulidae'
p5c5.order = 'Order: Nectridea'
p5c5.class_ = 'Subclass: Lepospondyli'
p5c5.phylum = 'Phylum: Chordata'
p5c5.prestige = 'Prestige: *** / ***'
p5c5.min_length = 3
p5c5.max_length_increment = 100
p5c5.min_weight = 20
p5c5.max_weight_increment = 1000
p5c5.description = 'Lepospondyl amphibians that lived from the Late Carboniferous to the Late Permian. Diplocaulus is the best known lepospondyls with a dinstinctive boomerang-shaped skull.'
p5c5.rarity = 2

# PERMIAN PERIOD CREATURES #
p6c1 = Creature()
p6c2 = Creature()
p6c3 = Creature()
p6c4 = Creature()
p6c5 = Creature()

p6c1.add_image(branchiosaurus_img)
p6c1.id = 25
p6c1.genus = 'Genus: Branchiosaurus'
p6c1.family = 'Family: Branchiosauridae'
p6c1.order = 'Order: Temnospondyli'
p6c1.class_ = 'Class: Amphibia'
p6c1.phylum = 'Phylum: Chordata'
p6c1.prestige = 'Prestige: * / ***'
p6c1.min_length = 1
p6c1.max_length_increment = 100
p6c1.min_weight = 1.8
p6c1.max_weight_increment = 60
p6c1.description = 'Small amphibian from the Carboniferous to Permian.'
p6c1.rarity = 0

p6c2.add_image(eryops_img)
p6c2.id = 26
p6c2.genus = 'Genus: Eryops'
p6c2.family = 'Family: Eryopidae'
p6c2.order = 'Order: Temnospondyli'
p6c2.class_ = 'Class: Amphibia'
p6c2.phylum = 'Phylum: Chordata'
p6c2.prestige = 'Prestige: * / ***'
p6c2.min_length = 5
p6c2.max_length_increment = 300
p6c2.min_weight = 225
p6c2.max_weight_increment = 17500
p6c2.description = 'Amphibian that was one of the largest land animals of the Permian. The Eryops had enormous mouths with curved teeth like that of the modern frog.'
p6c2.rarity = 0

p6c3.add_image(prionosuchus_img)
p6c3.id = 27
p6c3.genus = 'Genus: Prionosuchus'
p6c3.family = 'Family: Archegosauridae'
p6c3.order = 'Order: Temnospondyli'
p6c3.class_ = 'Class: Amphibia'
p6c3.phylum = 'Phylum: Chordata'
p6c3.prestige = 'Prestige: ** / ***'
p6c3.min_length = 18
p6c3.max_length_increment = 200
p6c3.min_weight = 1000
p6c3.max_weight_increment = 80000
p6c3.description = 'Genus of large temnospondyl with elongated, tapered snouts, a long body, and sharp teeth. This predator likely used ambush-style feeding.'
p6c3.rarity = 1

p6c4.add_image(stereosternum_img)
p6c4.id = 28
p6c4.genus = 'Genus: Stereosternum'
p6c4.family = 'Family: Mesosauridae'
p6c4.order = 'Order: Mesosauria'
p6c4.class_ = 'Class: Reptilia'
p6c4.phylum = 'Phylum: Chordata'
p6c4.prestige = 'Prestige: ** / ***'
p6c4.min_length = 2
p6c4.max_length_increment = 100
p6c4.min_weight = 7
p6c4.max_weight_increment = 200
p6c4.description = 'Genus of mesosaur reptile form the Early Permian. The Stereosternum were active aquatic predators.'
p6c4.rarity = 1

p6c5.add_image(lebachacanthus_img)
p6c5.id = 29
p6c5.genus = 'Genus: Lebachacanthus'
p6c5.family = 'Family: Diplodoselachidae'
p6c5.order = 'Order: Xenacanthida'
p6c5.class_ = 'Class: Chondrichthyes'
p6c5.phylum = 'Phylum: Chordata'
p6c5.prestige = 'Prestige: *** / ***'
p6c5.min_length = 8
p6c5.max_length_increment = 400
p6c5.min_weight = 200
p6c5.max_weight_increment = 10000
p6c5.description = 'Genus of xenacanthid shark from the Early Permian that ruled freshwater swamps and bogs. The Lebachacanthus was widespread around the globe and preyed on small amphibian-like animals.'
p6c5.rarity = 2


creatures_list = []
for i in range(6):
    row = []
    for j in range(5):
        row.append(Creature())
    creatures_list.append(row)

creatures_list[0][0] = p1c1
creatures_list[0][1] = p1c2
creatures_list[0][2] = p1c3
creatures_list[0][3] = p1c4
creatures_list[0][4] = p1c5

creatures_list[1][0] = p2c1
creatures_list[1][1] = p2c2
creatures_list[1][2] = p2c3
creatures_list[1][3] = p2c4
creatures_list[1][4] = p2c5

creatures_list[2][0] = p3c1
creatures_list[2][1] = p3c2
creatures_list[2][2] = p3c3
creatures_list[2][3] = p3c4
creatures_list[2][4] = p3c5

creatures_list[3][0] = p4c1
creatures_list[3][1] = p4c2
creatures_list[3][2] = p4c3
creatures_list[3][3] = p4c4
creatures_list[3][4] = p4c5

creatures_list[4][0] = p5c1
creatures_list[4][1] = p5c2
creatures_list[4][2] = p5c3
creatures_list[4][3] = p5c4
creatures_list[4][4] = p5c5

creatures_list[5][0] = p6c1
creatures_list[5][1] = p6c2
creatures_list[5][2] = p6c3
creatures_list[5][3] = p6c4
creatures_list[5][4] = p6c5