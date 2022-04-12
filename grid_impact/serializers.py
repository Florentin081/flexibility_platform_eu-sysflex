"""
Copyright 2021 AKKA Technologies (philippe.szczech@akka.eu)

Licensed under the EUPL, Version 1.2 or – as soon they will be approved by
the European Commission - subsequent versions of the EUPL (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence at:

https://joinup.ec.europa.eu/software/page/eupl

Unless required by applicable law or agreed to in writing, software
distributed under the Licence is distributed on an "AS IS" basis,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the Licence for the specific language governing permissions and
limitations under the Licence.
"""

from rest_framework import serializers

from .models import *


class BidGridImpactAssessmentResultSerializer(serializers.ModelSerializer):
    system_operator_name = serializers.ReadOnlyField(source='system_operator.identification')
    bid_name = serializers.SerializerMethodField()

    @staticmethod
    def get_bid_name(obj):
        return "bid_{}_{}".format(obj.bid.product.product_name, obj.bid.id)

    class Meta:
        model = BiddingGridImpactAssessmentResult
        fields = "__all__"
