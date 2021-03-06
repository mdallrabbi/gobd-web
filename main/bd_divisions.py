"""
List of Bangladesh Divisions, Districts and Upazilas/Thanas.
"""

from django.utils.translation import ugettext_lazy as _


# Reference: http://www.statoids.com/ubd.html

DIVISION_CHOICES = (
    ('BD.BA', _('Barisal')),
    ('BD.CG', _('Chittagong')),
    ('BD.DA', _('Dhaka')),
    ('BD.KH', _('Khulna')),
    ('BD.RS', _('Rajshahi')),
    ('BD.RP', _('Rangpur')),
    ('BD.SY', _('Sylhet')),
)

# Reference: http://www.statoids.com/ybd.html

DISTRICT_CHOICES = (
    ('BD.KH.BH', _('Bagerhat')),
    ('BD.CG.BD', _('Bandarban')),
    ('BD.BA.BG', _('Barguna')),
    ('BD.BA.BS', _('Barisal')),
    ('BD.BA.BL', _('Bhola')),
    ('BD.RS.BO', _('Bogra')),
    ('BD.CG.BB', _('Brahmanbaria')),
    ('BD.CG.CP', _('Chandpur')),
    ('BD.CG.CT', _('Chittagong')),
    ('BD.KH.CD', _('Chuadanga')),
    ('BD.CG.CM', _('Comilla')),
    ('BD.CG.CB', _("Cox's Bazar")),
    ('BD.DA.DH', _('Dhaka')),
    ('BD.RP.DJ', _('Dinajpur')),
    ('BD.DA.FR', _('Faridpur')),
    ('BD.CG.FN', _('Feni')),
    ('BD.RP.GB', _('Gaibandha')),
    ('BD.DA.GZ', _('Gazipur')),
    ('BD.DA.GG', _('Gopalganj')),
    ('BD.SY.HA', _('Habiganj')),
    ('BD.RS.JP', _('Jaipurhat')),
    ('BD.DA.JM', _('Jamalpur')),
    ('BD.KH.JS', _('Jessore')),
    ('BD.BA.JK', _('Jhalakati')),
    ('BD.KH.JN', _('Jhenaidah')),
    ('BD.CG.KG', _('Khagrachari')),
    ('BD.KH.KL', _('Khulna')),
    ('BD.DA.KS', _('Kishoreganj')),
    ('BD.RP.KR', _('Kurigram')),
    ('BD.KH.KU', _('Kushtia')),
    ('BD.CG.LK', _('Lakshmipur')),
    ('BD.RP.LL', _('Lalmonirhat')),
    ('BD.DA.MD', _('Madaripur')),
    ('BD.KH.MG', _('Magura')),
    ('BD.DA.MK', _('Manikganj')),
    ('BD.KH.ME', _('Meherpur')),
    ('BD.SY.MB', _('Moulvibazar')),
    ('BD.DA.MU', _('Munshiganj')),
    ('BD.DA.MM', _('Mymensingh')),
    ('BD.RS.NA', _('Naogaon')),
    ('BD.KH.NR', _('Narail')),
    ('BD.DA.NY', _('Narayanganj')),
    ('BD.DA.NS', _('Narsingdi')),
    ('BD.RS.NT', _('Natore')),
    ('BD.RS.NW', _('Nawabganj')),
    ('BD.DA.NK', _('Netrakona')),
    ('BD.RP.NP', _('Nilphamari')),
    ('BD.CG.NO', _('Noakhali')),
    ('BD.RS.PB', _('Pabna')),
    ('BD.RP.PN', _('Panchagarh')),
    ('BD.CG.PC', _('Parbattya Chattagram')),
    ('BD.BA.PT', _('Patuakhali')),
    ('BD.BA.PR', _('Pirojpur')),
    ('BD.DA.RB', _('Rajbari')),
    ('BD.RS.RS', _('Rajshahi')),
    ('BD.RP.RP', _('Rangpur')),
    ('BD.KH.ST', _('Satkhira')),
    ('BD.DA.SA', _('Shariatpur')),
    ('BD.DA.SP', _('Sherpur')),
    ('BD.RS.SR', _('Sirajganj')),
    ('BD.SY.SN', _('Sunamganj')),
    ('BD.SY.SL', _('Sylhet')),
    ('BD.DA.TA', _('Tangail')),
    ('BD.RP.TH', _('Thakurgaon')),
)

# Reference: http://www.pmo.gov.bd/pmolib/maps/index.html

UPAZILA_CHOICES = (
    ('000', _('Abhaynagar')),
    ('001', _('Adamdighi')),
    ('002', _('Aditmari')),
    ('003', _('Agailjhara')),
    ('004', _('Ajmiriganj')),
    ('005', _('Akhaura')),
    ('006', _('Akkelpur')),
    ('007', _('Alamdanga')),
    ('008', _('Ali Kadam')),
    ('009', _('Amtali')),
    ('010', _('Anwara')),
    ('011', _('Araihazar')),
    ('012', _('Ashuganj')),
    ('013', _('Astagram')),
    ('014', _('Atgharia')),
    ('015', _('Atpara')),
    ('016', _('Atrai')),
    ('017', _('Atwari')),
    ('018', _('Babuganj')),
    ('019', _('Badalgachhi')),
    ('020', _('Badarganj')),
    ('021', _('Badda Thana')),
    ('022', _('Bagaichhari')),
    ('023', _('Bagatipara')),
    ('024', _('Bagerhat Sadar')),
    ('025', _('Bagha')),
    ('026', _('Bagherpara')),
    ('027', _('Bagmara')),
    ('028', _('Bahubal')),
    ('029', _('Bajitpur')),
    ('030', _('Bakerganj')),
    ('031', _('Baksiganj')),
    ('032', _('Balaganj')),
    ('033', _('Baliadangi')),
    ('034', _('Baliakandi')),
    ('035', _('Bamna')),
    ('036', _('Banaripara')),
    ('037', _('Bancharampur')),
    ('038', _('Bandar')),
    ('039', _('Bandarban Sadar')),
    ('040', _('Baniyachong')),
    ('041', _('Banshkhali')),
    ('042', _('Baraigram')),
    ('043', _('Barguna Sadar')),
    ('044', _('Barhatta')),
    ('045', _('Barisal Sadar')),
    ('046', _('Barkal')),
    ('047', _('Barlekha')),
    ('048', _('Barura')),
    ('049', _('Basail')),
    ('050', _('Batiaghata')),
    ('051', _('Bauphal')),
    ('052', _('Beanibazar')),
    ('053', _('Begumganj')),
    ('054', _('Belabo')),
    ('055', _('Belaichhari')),
    ('056', _('Belkuchi')),
    ('057', _('Bera')),
    ('058', _('Betagi')),
    ('059', _('Bhairab')),
    ('060', _('Bhaluka')),
    ('061', _('Bhandaria')),
    ('062', _('Bhangura')),
    ('063', _('Bhedarganj')),
    ('064', _('Bheramara')),
    ('065', _('Bhola Sadar')),
    ('066', _('Bholahat')),
    ('067', _('Bhuapur')),
    ('068', _('Bhurungamari')),
    ('069', _('Biral')),
    ('070', _('Birampur')),
    ('071', _('Birganj')),
    ('072', _('Bishwamvarpur')),
    ('073', _('Biswanath')),
    ('074', _('Boalia Thana')),
    ('075', _('Boalkhali')),
    ('076', _('Bochaganj')),
    ('077', _('Boda')),
    ('078', _('Bogra Sadar')),
    ('079', _('Brahmanbaria Sadar')),
    ('080', _('Brahmanpara')),
    ('081', _('Burhanuddin')),
    ('082', _('Burichong')),
    ('083', _('Cantonnent Thana')),
    ('084', _('Chakaria')),
    ('085', _('Chandanaish')),
    ('086', _('Chandina')),
    ('087', _('Chandpur Sadar')),
    ('088', _('Char Fasson')),
    ('089', _('Char Rajibpur')),
    ('090', _('Charghat')),
    ('091', _('Chatkhil')),
    ('092', _('Chatmohar')),
    ('093', _('Chauddagram')),
    ('094', _('Chaugachha')),
    ('095', _('Chauhali')),
    ('096', _('Chhagalnaiya')),
    ('097', _('Chhatak')),
    ('098', _('Chilmari')),
    ('099', _('Chirirbandar')),
    ('100', _('Chitalmari')),
    ('101', _('Chuadanga Sadar')),
    ('102', _('Chunarughat')),
    ('103', _('Comilla Sadar')),
    ('104', _('Companiganj')),
    ('105', _('Companiganj, Noakhali')),
    ('106', _("Cox's Bazar Sadar")),
    ('107', _('Dacope')),
    ('108', _('Daganbhuiyan')),
    ('109', _('Damudya')),
    ('110', _('Damurhuda')),
    ('111', _('Dasmina')),
    ('112', _('Daudkandi')),
    ('113', _('Daulatkhan')),
    ('114', _('Daulatpur')),
    ('115', _('Daulatpur, Kushtia')),
    ('116', _('Daulatpur Thana')),
    ('117', _('Debiganj')),
    ('118', _('Delduar')),
    ('119', _('Demra Thana')),
    ('120', _('Derai')),
    ('121', _('Devidwar')),
    ('122', _('Dewanganj')),
    ('123', _('Dhamoirhat')),
    ('124', _('Dhamrai')),
    ('125', _('Dhanbari')),
    ('126', _('Dhanmandi Thana')),
    ('127', _('Dharampasha')),
    ('128', _('Dhobaura')),
    ('129', _('Dhunat')),
    ('130', _('Dighalia')),
    ('131', _('Dighinala')),
    ('132', _('Dimla')),
    ('133', _('Dinajpur Sadar')),
    ('134', _('Dohar')),
    ('135', _('Domar')),
    ('136', _('Dowarabazar')),
    ('137', _('Dumuria')),
    ('138', _('Dupchanchia')),
    ('139', _('Durgapur')),
    ('140', _('Durgapur, Rajshahi')),
    ('141', _('Fakirhat')),
    ('142', _('Faridganj')),
    ('143', _('Faridpur')),
    ('144', _('Fatikchhari')),
    ('145', _('Fenchuganj')),
    ('146', _('Feni Sadar')),
    ('147', _('Fulgazi')),
    ('148', _('Gabtali')),
    ('149', _('Gaffargaon')),
    ('150', _('Gaibandha Sadar')),
    ('151', _('Galachipa')),
    ('152', _('Gangachhara')),
    ('153', _('Gangni')),
    ('154', _('Gauripur')),
    ('155', _('Gaurnadi')),
    ('156', _('Gazaria')),
    ('157', _('Gazipur Sadar')),
    ('158', _('Ghatail')),
    ('159', _('Ghior')),
    ('160', _('Ghoraghat')),
    ('161', _('Goalandaghat')),
    ('162', _('Gobindaganj')),
    ('163', _('Godagari')),
    ('164', _('Golapganj')),
    ('165', _('Gomastapur')),
    ('166', _('Gopalganj Sadar')),
    ('167', _('Gopalpur')),
    ('168', _('Gosairhat')),
    ('169', _('Gowainghat')),
    ('170', _('Gulshan Thana')),
    ('171', _('Gurudaspur')),
    ('172', _('Habiganj Sadar')),
    ('173', _('Haimchar')),
    ('174', _('Hakimpur')),
    ('175', _('Haluaghat')),
    ('176', _('Harinakunda')),
    ('177', _('Haripur')),
    ('178', _('Harirampur')),
    ('179', _('Hathazari')),
    ('180', _('Hatibandha')),
    ('181', _('Hatiya')),
    ('182', _('Hazaribagh Thana')),
    ('183', _('Haziganj')),
    ('184', _('Hizla')),
    ('185', _('Homna')),
    ('186', _('Hossainpur')),
    ('187', _('Ishwardi')),
    ('188', _('Ishwarganj')),
    ('189', _('Islampur')),
    ('190', _('Itna')),
    ('191', _('Jagannathpur')),
    ('192', _('Jaintiapur')),
    ('193', _('Jaldhaka')),
    ('194', _('Jamalganj')),
    ('195', _('Jamalpur Sadar')),
    ('196', _('Jessore Sadar')),
    ('197', _('Jhalokati Sadar')),
    ('198', _('Jhenaidah Sadar')),
    ('199', _('Jhenaigati')),
    ('200', _('Jhikargachha')),
    ('201', _('Jibannagar')),
    ('202', _('Joypurhat Sadar')),
    ('203', _('Juraichhari')),
    ('204', _('Juri')),
    ('205', _('Kachua')),
    ('206', _('Kachua, Bagerhat')),
    ('207', _('Kafrul Thana')),
    ('208', _('Kahaloo')),
    ('209', _('Kaharole')),
    ('210', _('Kalai')),
    ('211', _('Kalapara')),
    ('212', _('Kalia')),
    ('213', _('Kaliakair')),
    ('214', _('Kaliganj, Gazipur')),
    ('215', _('Kaliganj, Jhenaidah')),
    ('216', _('Kaliganj, Lalmonirhat')),
    ('217', _('Kalihati')),
    ('218', _('Kalkini')),
    ('219', _('Kalmakanda')),
    ('220', _('Kamalganj')),
    ('221', _('Kamarkhanda')),
    ('222', _('Kamrangir Char')),
    ('223', _('Kanaighat')),
    ('224', _('Kapasia')),
    ('225', _('Kaptai')),
    ('226', _('Karimganj')),
    ('227', _('Kasba')),
    ('228', _('Kashiani')),
    ('229', _('Kathalia')),
    ('230', _('Katiadi')),
    ('231', _('Kaunia')),
    ('232', _('Kawkhali')),
    ('233', _('Kawkhali (Betbunia)')),
    ('234', _('Kazipur')),
    ('235', _('Kendua')),
    ('236', _('Keraniganj  (Dhaka)')),
    ('237', _('Khagrachhari')),
    ('238', _('Khaliajuri')),
    ('239', _('Khalishpur Thana')),
    ('240', _('Khanjahan Ali Thana')),
    ('241', _('Khansama')),
    ('242', _('Khetlal')),
    ('243', _('Khilgaon Thana')),
    ('244', _('Khoksa')),
    ('245', _('Kishoreganj')),
    ('246', _('Kishoreganj Sadar')),
    ('247', _('Komolnagor')),
    ('248', _('Kotalipara')),
    ('249', _('Kotchandpur')),
    ('250', _('Kotoali Thana')),
    ('251', _('Kotwali Thana')),
    ('252', _('Koyra')),
    ('253', _('Kulaura')),
    ('254', _('Kuliarchar')),
    ('255', _('Kumarkhali')),
    ('256', _('Kurigram Sadar')),
    ('257', _('Kushtia Sadar')),
    ('258', _('Kutubdia')),
    ('259', _('Lakhai')),
    ('260', _('Laksam')),
    ('261', _('Lakshmichhari')),
    ('262', _('Lakshmipur Sadar')),
    ('263', _('Lalbagh Thana')),
    ('264', _('Lalmohan')),
    ('265', _('Lalmonirhat Sadar')),
    ('266', _('Lalpur')),
    ('267', _('Lama')),
    ('268', _('Langadu')),
    ('269', _('Lohaganj')),
    ('270', _('Lohagara')),
    ('271', _('Lohagara, Narail')),
    ('272', _('Madan')),
    ('273', _('Madarganj')),
    ('274', _('Madaripur Sadar')),
    ('275', _('Madhabpur')),
    ('276', _('Madhupur')),
    ('277', _('Magura Sadar')),
    ('278', _('Mahadevpur')),
    ('279', _('Mahalchhari')),
    ('280', _('Maheshkhali')),
    ('281', _('Maheshpur')),
    ('282', _('Manda')),
    ('283', _('Manikchhari')),
    ('284', _('Manikganj Sadar')),
    ('285', _('Manirampur')),
    ('286', _('Mannerchar')),
    ('287', _('Manpura')),
    ('288', _('Mathbaria')),
    ('289', _('Matihar Thana')),
    ('290', _('Matiranga')),
    ('291', _('Matlab')),
    ('292', _('Matlab Uttor')),
    ('293', _('Maulvibazar Sadar')),
    ('294', _('Mehendiganj')),
    ('295', _('Meherpur Sadar')),
    ('296', _('Melandaha')),
    ('297', _('Mirpur')),
    ('298', _('Mirpur Thana')),
    ('299', _('Mirsharai')),
    ('300', _('Mirzaganj')),
    ('301', _('Mirzapur')),
    ('302', _('Mithamain')),
    ('303', _('Mithapukur')),
    ('304', _('Mohammadpur')),
    ('305', _('Mohammadpur Thana')),
    ('306', _('Mohanganj')),
    ('307', _('Mohanpur')),
    ('308', _('Mollahat')),
    ('309', _('Mongla')),
    ('310', _('Monohardi')),
    ('311', _('Morrelganj')),
    ('312', _('Motijheel Thana')),
    ('313', _('Mujibnagar')),
    ('314', _('Muksudpur')),
    ('315', _('Muktagachha')),
    ('316', _('Muladi')),
    ('317', _('Munshiganj Sadar')),
    ('318', _('Muradnagar')),
    ('319', _('Mymensingh Sadar')),
    ('320', _('Nabiganj')),
    ('321', _('Nabinagar')),
    ('322', _('Nachole')),
    ('323', _('Nagarpur')),
    ('324', _('Nageshwari')),
    ('325', _('Naikhongchhari')),
    ('326', _('Nakla')),
    ('327', _('Nalchity')),
    ('328', _('Nalitabari')),
    ('329', _('Nandail')),
    ('330', _('Nandigram')),
    ('331', _('Nangalkot')),
    ('332', _('Naogaon Sadar')),
    ('333', _('Narail Sadar')),
    ('334', _('Narayanganj Sadar')),
    ('335', _('Naria')),
    ('336', _('Narsingdi Sadar')),
    ('337', _('Nasirnagar')),
    ('338', _('Natore Sadar')),
    ('339', _('Nawabganj  (Dhaka)')),
    ('340', _('Nawabganj, Dinajpur')),
    ('341', _('Nawabganj Sadar')),
    ('342', _('Nazirpur')),
    ('343', _('Nesarabad (Swarupkati)')),
    ('344', _('Netrokona Sadar')),
    ('345', _('Niamatpur')),
    ('346', _('Nikli')),
    ('347', _('Nilphamari Sadar')),
    ('348', _('Noakhali Sadar')),
    ('349', _('Paba')),
    ('350', _('Pabna Sadar')),
    ('351', _('Paikgachha')),
    ('352', _('Pakundia')),
    ('353', _('Palash')),
    ('354', _('Palashbari')),
    ('355', _('Pallabi Thana')),
    ('356', _('Panchagarh Sadar')),
    ('357', _('Panchbibi')),
    ('358', _('Panchhari')),
    ('359', _('Pangsha')),
    ('360', _('Parbatipur')),
    ('361', _('Parshuram')),
    ('362', _('Patgram')),
    ('363', _('Patharghata')),
    ('364', _('Patiya')),
    ('365', _('Patnitala')),
    ('366', _('Patuakhali Sadar')),
    ('367', _('Phulbari, Dinajpur')),
    ('368', _('Phulbari, Kurigram')),
    ('369', _('Phulbari, Mymensingh')),
    ('370', _('Phulchhari')),
    ('371', _('Phulpur')),
    ('372', _('Phultoli')),
    ('373', _('Pirgachha')),
    ('374', _('Pirganj')),
    ('375', _('Pirganj, Thakurgaon')),
    ('376', _('Pirojpur Sadar')),
    ('377', _('Porsha')),
    ('378', _('Purbadhala Upazil')),
    ('379', _('Puthia')),
    ('380', _('Raiganj')),
    ('381', _('Raipur')),
    ('382', _('Raipura, Narsingdi')),
    ('383', _('Rajapur')),
    ('384', _('Rajarhat')),
    ('385', _('Rajasthali')),
    ('386', _('Rajbari Sadar')),
    ('387', _('Rajnagar')),
    ('388', _('Rajoir')),
    ('389', _('Rajpara Thana')),
    ('390', _('Ramganj')),
    ('391', _('Ramgarh')),
    ('392', _('Ramgati')),
    ('393', _('Ramna Thana')),
    ('394', _('Rampal')),
    ('395', _('Ramu')),
    ('396', _('Rangamati Sadar')),
    ('397', _('Rangpur Sadar')),
    ('398', _('Rangunia')),
    ('399', _('Raninagar')),
    ('400', _('Ranisankail')),
    ('401', _('Raomari')),
    ('402', _('Raozan')),
    ('403', _('Rowangchhari')),
    ('404', _('Rujganj')),
    ('405', _('Ruma')),
    ('406', _('Rupsha')),
    ('407', _('Sabujbagh Thana')),
    ('408', _('Sadullapur')),
    ('409', _('Sahajanpur')),
    ('410', _('Saidpur')),
    ('411', _('Sakhipur')),
    ('412', _('Sandwip')),
    ('413', _('Santhia')),
    ('414', _('Sapahar')),
    ('415', _('Sarail')),
    ('416', _('Sarankhola')),
    ('417', _('Sariakandi')),
    ('418', _('Sarishabari')),
    ('419', _('Satkania')),
    ('420', _('Saturia')),
    ('421', _('Savar  (Dhaka)')),
    ('422', _('Senbagh')),
    ('423', _('Shahjadpur')),
    ('424', _('Shahmokhdum Thana')),
    ('425', _('Shahrasti')),
    ('426', _('Shailkupa')),
    ('427', _('Shalikha')),
    ('428', _('Shampur Thana')),
    ('429', _('Shariatpur Sadar')),
    ('430', _('Sharsha')),
    ('431', _('Sherpur')),
    ('432', _('Sherpur Sadar')),
    ('433', _('Shibchar')),
    ('434', _('Shibganj')),
    ('435', _('Shibganj, Nawabganj')),
    ('436', _('Shibpur')),
    ('437', _('Shivalaya')),
    ('438', _('Singair')),
    ('439', _('Singra')),
    ('440', _('Sirajdikhan')),
    ('441', _('Sirajganj Sadar')),
    ('442', _('Sitakunda')),
    ('443', _('Sonadanga Thana')),
    ('444', _('Sonagazi')),
    ('445', _('Sonargaon')),
    ('446', _('Sonatala')),
    ('447', _('South Surma')),
    ('448', _('Sreebardi')),
    ('449', _('Sreemangal')),
    ('450', _('Sreenagar')),
    ('451', _('Sreepur')),
    ('452', _('Sreepur, Magura')),
    ('453', _('Sughatta')),
    ('454', _('Sujanagar')),
    ('455', _('Sullah')),
    ('456', _('Sunamganj Sadar')),
    ('457', _('Sundarganj')),
    ('458', _('Sutrapur Thana')),
    ('459', _('Sylhet Sadar')),
    ('460', _('Tahirpur')),
    ('461', _('Tangail Sadar')),
    ('462', _('Tanore')),
    ('463', _('Taraganj')),
    ('464', _('Tarail')),
    ('465', _('Tarash')),
    ('466', _('Tazumuddin')),
    ('467', _('Tejgaon Thana')),
    ('468', _('Teknaf')),
    ('469', _('Terokhada')),
    ('470', _('Tetulia')),
    ('471', _('Thakurgaon Sadar')),
    ('472', _('Thanchi')),
    ('473', _('Tongibari')),
    ('474', _('Trishal')),
    ('475', _('Tungipara')),
    ('476', _('Ukhia')),
    ('477', _('Ulipur')),
    ('478', _('Ullahpara')),
    ('479', _('Uttra Thana')),
    ('480', _('Wazirpur')),
    ('481', _('Zakiganj')),
    ('482', _('Zanjira')),
)


