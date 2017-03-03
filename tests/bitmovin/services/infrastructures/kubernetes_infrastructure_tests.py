import unittest
import json
from bitmovin import Bitmovin, Response, KubernetesInfrastructure
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class KubernetesInfrastructureTests(BitmovinTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        self.bitmovin = Bitmovin(self.api_key)
        self.assertIsNotNone(self.bitmovin)
        self.assertTrue(isinstance(self.bitmovin, Bitmovin))

    def tearDown(self):
        super().tearDown()

    def test_create_k8s_infrastructure(self):
        k8s_infrastructure = self._get_sample_k8s_infrastructure()
        k8s_infrastructure_response = self.bitmovin.infrastructures.Kubernetes.create(object_=k8s_infrastructure)
        self.assertIsNotNone(k8s_infrastructure_response)
        self.assertIsNotNone(k8s_infrastructure_response.resource)
        self.assertIsNotNone(k8s_infrastructure_response.resource.id)
        self._compare_k8s_infrastructures(k8s_infrastructure, k8s_infrastructure_response.resource)

    def test_retrieve_k8s_infrastructure(self):
        k8s_infrastructure = self._get_sample_k8s_infrastructure()
        k8s_infrastructure_response = self.bitmovin.infrastructures.Kubernetes.create(object_=k8s_infrastructure)
        self.assertIsNotNone(k8s_infrastructure_response)
        self.assertIsNotNone(k8s_infrastructure_response.resource)
        self.assertIsNotNone(k8s_infrastructure_response.resource.id)
        self._compare_k8s_infrastructures(k8s_infrastructure, k8s_infrastructure_response.resource)

        retrieved_k8s_infrastructure = self.bitmovin.infrastructures.Kubernetes.retrieve(
            k8s_infrastructure_response.resource.id)
        self.assertIsNotNone(retrieved_k8s_infrastructure)
        self.assertIsNotNone(retrieved_k8s_infrastructure.resource)
        self._compare_k8s_infrastructures(k8s_infrastructure_response.resource, retrieved_k8s_infrastructure.resource)

    def test_delete_k8s_infrastructure(self):
        k8s_infrastructure = self._get_sample_k8s_infrastructure()
        k8s_infrastructure_response = self.bitmovin.infrastructures.Kubernetes.create(object_=k8s_infrastructure)
        self.assertIsNotNone(k8s_infrastructure_response)
        self.assertIsNotNone(k8s_infrastructure_response.resource)
        self.assertIsNotNone(k8s_infrastructure_response.resource.id)
        self._compare_k8s_infrastructures(k8s_infrastructure, k8s_infrastructure_response.resource)

        deleted_minimal_resource = self.bitmovin.infrastructures.Kubernetes.delete(
            k8s_infrastructure_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.infrastructures.Kubernetes.retrieve(k8s_infrastructure_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving filter after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_k8s_infrastructures(self):
        k8s_infrastructure = self._get_sample_k8s_infrastructure()
        k8s_infrastructure_response = self.bitmovin.infrastructures.Kubernetes.create(object_=k8s_infrastructure)
        self.assertIsNotNone(k8s_infrastructure_response)
        self.assertIsNotNone(k8s_infrastructure_response.resource)
        self.assertIsNotNone(k8s_infrastructure_response.resource.id)
        self._compare_k8s_infrastructures(k8s_infrastructure, k8s_infrastructure_response.resource)

        infrastructures = self.bitmovin.infrastructures.Kubernetes.list()
        self.assertIsNotNone(infrastructures)
        self.assertIsNotNone(infrastructures.resource)
        self.assertIsNotNone(infrastructures.response)
        self.assertIsInstance(infrastructures.resource, list)
        self.assertIsInstance(infrastructures.response, Response)
        self.assertGreater(infrastructures.resource.__sizeof__(), 1)

    def test_retrieve_k8s_infrastructure_custom_data(self):
        k8s_infrastructure = self._get_sample_k8s_infrastructure()
        k8s_infrastructure.customData = '<pre>my custom data</pre>'
        k8s_infrastructure_response = self.bitmovin.infrastructures.Kubernetes.create(object_=k8s_infrastructure)
        self.assertIsNotNone(k8s_infrastructure_response)
        self.assertIsNotNone(k8s_infrastructure_response.resource)
        self.assertIsNotNone(k8s_infrastructure_response.resource.id)
        self._compare_k8s_infrastructures(k8s_infrastructure, k8s_infrastructure_response.resource)

        custom_data_response = self.bitmovin.infrastructures.Kubernetes.retrieve_custom_data(
            k8s_infrastructure_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(k8s_infrastructure.customData, json.loads(custom_data.customData))

    def _compare_k8s_infrastructures(self, first: KubernetesInfrastructure, second: KubernetesInfrastructure):
        """

        :param first: RotateFilter
        :param second: RotateFilter
        :return: bool
        """
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _get_sample_k8s_infrastructure(self):
        k8s_infrastructure = KubernetesInfrastructure(name='TestInfrastructure', description='Bitmovin Python Test')
        self.assertIsNotNone(k8s_infrastructure.name)
        self.assertIsNotNone(k8s_infrastructure.description)
        return k8s_infrastructure


if __name__ == '__main__':
    unittest.main()
