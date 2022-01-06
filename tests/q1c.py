test = {   'name': 'q1c',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> reconstructed = reconstruct_raw_labels(process_labels(raw_labels[0, np.newaxis]))\n'
                                               '>>> # Check that all reconstructed labels are present in the raw labels\n'
                                               '>>> matches = np.all((reconstructed[0][:, np.newaxis] == raw_labels[0]), axis=2)\n'
                                               '>>> matches.sum() == len(reconstructed[0]) and len(reconstructed[0]) > 0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
