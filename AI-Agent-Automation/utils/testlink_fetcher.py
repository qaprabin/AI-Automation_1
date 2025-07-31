from testlink import TestlinkAPIClient

class TestLinkConnector:
    def __init__(self):
        self.url = 'http://192.168.6.243:81/testlink/index.php'
        self.dev_key = 'ceaf407342176e24abba2be65983d35a'
        self.client = TestlinkAPIClient(self.url, self.dev_key)

    def get_test_steps(self, project_name, test_case_name):
        # Fetch test cases under the given project
        test_cases = self.client.getTestCase(None, testprojectname=project_name)

        for case in test_cases:
            if case['name'] == test_case_name:
                steps = case.get('steps', [])
                return [step['actions'] for step in steps]

        print(f"❌ Test case '{test_case_name}' not found in project '{project_name}'")
        return []
