# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateChannelRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'CreateChannel')

	def get_Organizations(self):
		return self.get_query_params().get('Organizations')

	def set_Organizations(self,Organizations):
		for i in range(len(Organizations)):	
			if Organizations[i].get('Id') is not None:
				self.add_query_param('Organization.' + str(i + 1) + '.Id' , Organizations[i].get('Id'))


	def get_ChannelName(self):
		return self.get_query_params().get('ChannelName')

	def set_ChannelName(self,ChannelName):
		self.add_query_param('ChannelName',ChannelName)

	def get_ConsortiumId(self):
		return self.get_query_params().get('ConsortiumId')

	def set_ConsortiumId(self,ConsortiumId):
		self.add_query_param('ConsortiumId',ConsortiumId)