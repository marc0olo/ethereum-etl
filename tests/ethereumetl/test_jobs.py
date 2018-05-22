# TODO: Read from file
from ethereumetl.job.export_blocks_job import ExportBlocksJob


class MockIPCWrapper(object):
    def make_request(self, text):
        return [{
            'result': {
                'author': '0x0000000000000000000000000000000000000000',
                'difficulty': '0x400000000',
                'extraData': '0x11bbe8db4e347b4e8c937c1c8370e4b5ed33adb3db69cbdb7a38e1e50b1b82fa',
                'gasLimit': '0x1388',
                'gasUsed': '0x0',
                'hash': '0xd4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3',
                'logsBloom': '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
                'miner': '0x0000000000000000000000000000000000000000',
                'mixHash': '0x0000000000000000000000000000000000000000000000000000000000000000',
                'nonce': '0x0000000000000042',
                'number': '0x0',
                'parentHash': '0x0000000000000000000000000000000000000000000000000000000000000000',
                'receiptsRoot': '0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421',
                'sha3Uncles': '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
                'size': '0x21c',
                'stateRoot': '0xd7f8974fb5ac78d9ac099b9ad5018bedc2ce0a72dad1827a1709da30580f0544',
                'timestamp': '0x0',
                'totalDifficulty': '0x400000000',
                'transactions': [],
                'transactionsRoot': '0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421',
                'uncles': []
            }
        }]


def test_export_blocks_job():
    job = ExportBlocksJob(
        start_block=0, end_block=0, batch_size=1, ipc_wrapper_factory=lambda: MockIPCWrapper(),
        blocks_output='test_jobs_blocks.csv'
    )
    job.run()

    # TODO: Check the result