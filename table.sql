-- public.tb_karyawan definition

-- Drop table

-- DROP TABLE public.tb_karyawan;

CREATE TABLE public.tb_karyawan (
	id serial NOT NULL DEFAULT nextval('tb_karyawan_id_seq'::regclass),
	nama varchar(50) NOT NULL,
	nik varchar(10) NOT NULL,
	face_data bytea NOT NULL,
	CONSTRAINT tb_karyawan_pkey PRIMARY KEY (id)
);


-- public.tb_absen definition

-- Drop table

-- DROP TABLE public.tb_absen;

CREATE TABLE public.tb_absen (
	id_absen serial NOT NULL DEFAULT nextval('tb_absen_id_absen_seq'::regclass),
	id_user int4 NOT NULL,
	absen_mode varchar(10) NOT NULL,
	waktu timestamp NOT NULL,
	CONSTRAINT tb_absen_pkey PRIMARY KEY (id_absen),
	CONSTRAINT tb_absen_id_user_fkey FOREIGN KEY (id_user) REFERENCES tb_karyawan(id)
);