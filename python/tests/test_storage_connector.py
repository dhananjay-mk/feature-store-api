#
#   Copyright 2021 Logical Clocks AB
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from hsfs.storage_connector import StorageConnector


class TestJdbcConnector:
    def test_spark_options_arguments_none(self):
        connection_string = (
            "jdbc:mysql://mysql_server_ip:1433;database=test;loginTimeout=30;"
        )

        jdbc_connector = StorageConnector(
            id=1,
            name="test_connector",
            featurestore_id=3,
            storage_connector_type="JDBC",
            connection_string=connection_string,
            arguments=None,
        )

        spark_options = jdbc_connector.spark_options()

        assert spark_options["url"] == connection_string

    def test_spark_options_arguments_empty(self):
        connection_string = (
            "jdbc:mysql://mysql_server_ip:1433;database=test;loginTimeout=30;"
        )

        jdbc_connector = StorageConnector(
            id=1,
            name="test_connector",
            featurestore_id=1,
            storage_connector_type="JDBC",
            connection_string=connection_string,
            arguments="",
        )

        spark_options = jdbc_connector.spark_options()

        assert spark_options["url"] == connection_string

    def test_spark_options_arguments_arguments(self):
        connection_string = (
            "jdbc:mysql://mysql_server_ip:1433;database=test;loginTimeout=30;"
        )
        arguments = "arg1=value1,arg2=value2"

        jdbc_connector = StorageConnector(
            id=1,
            name="test_connector",
            featurestore_id=1,
            storage_connector_type="JDBC",
            connection_string=connection_string,
            arguments=arguments,
        )

        spark_options = jdbc_connector.spark_options()

        assert spark_options["url"] == connection_string
        assert spark_options["arg1"] == "value1"
        assert spark_options["arg2"] == "value2"