# yapf: disable


checkname = 'oracle_asm_diskgroup'


info = [[None,
         'MOUNTED',
         'NORMAL',
         'N',
         '512',
         '4096',
         '1048576',
         '3072',
         '2146',
         '309',
         '918',
         '0',
         'Y',
         'OCR_VOTE/'],
        [None,
         'MOUNTED',
         'EXTERN',
         'FRA',
         '4096',
         '4194304',
         '0',
         '10236',
         '4468',
         'FRA01',
         'N',
         'REGULAR',
         '0',
         '8640000',
         '1'],
        [None,
         'DISMOUNTED',
         'EXTERN',
         'GRID',
         '4096',
         '4194304',
         '0',
         '5112',
         '5016',
         'GRID01',
         'N',
         'REGULAR',
         '0',
         '8640000',
         '1'],
        [None,
         'MOUNTED',
         'NORMAL',
         'DATA',
         '4096',
         '4194304',
         '102396',
         '614376',
         '476280',
         'NS1',
         'N',
         'REGULAR',
         '0',
         '8640000',
         '3']]


discovery = {'': [('DATA', {}), ('FRA', {}), ('GRID', {}), ('OCR_VOTE', {})]}


checks = {'': [('DATA',
                {'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'req_mir_free': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '22.48% used (134.86 of 599.98 GB), trend: 0 B / 24 hours, normal redundancy, 3 disks in 1 failgroups',
                  [('DATA', 138096, 491500.8, 552938.4, 0, 614376),
                   ('fs_size', 614376, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 25599)])]),
               ('FRA',
                {'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'req_mir_free': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '56.35% used (5.63 of 10 GB), trend: 0 B / 24 hours, extern redundancy, 1 disks',
                  [('FRA', 5768, 8188.8, 9212.4, 0, 10236),
                   ('fs_size', 10236, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 426)])]),
               ('GRID',
                {'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'req_mir_free': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(2, 'Diskgroup dismounted', [])]),
               ('OCR_VOTE',
                {'levels': (80.0, 90.0),
                 'levels_low': (50.0, 60.0),
                 'magic_normsize': 20,
                 'req_mir_free': False,
                 'trend_perfdata': True,
                 'trend_range': 24},
                [(0,
                  '30.18% used (309 MB of 1 GB), trend: 0 B / 24 hours, normal redundancy, old plugin data, possible wrong used and free space',
                  [('OCR_VOTE', 309, 819.2, 921.6, 0, 1024),
                   ('fs_size', 1024, None, None, None, None),
                   ('growth', 0.0, None, None, None, None),
                   ('trend', 0, None, None, 0, 42)])])]}