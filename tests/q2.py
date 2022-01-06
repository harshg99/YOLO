test = {   'name': 'q2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': ">>> loss_test_data = np.load('test_yolo_loss.npz')\n"
                                               ">>> pred = torch.tensor(loss_test_data['pred'], dtype=torch.float32)\n"
                                               ">>> target = torch.tensor(loss_test_data['target'], dtype=torch.float32)\n"
                                               ">>> loss = torch.tensor(loss_test_data['loss'], dtype=torch.float32)\n"
                                               '>>> \n'
                                               '>>> for i in range(10):\n'
                                               '...     print(torch.isclose(yolo_loss(pred[i], target[i]), loss[i]).item())\n'
                                               'True\n'
                                               'True\n'
                                               'True\n'
                                               'True\n'
                                               'True\n'
                                               'True\n'
                                               'True\n'
                                               'True\n'
                                               'True\n'
                                               'True\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
