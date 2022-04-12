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

from djongo import models

from bidding.models import FlexibilityBid
from flexibility_platform.models import SystemOperator


class BiddingGridImpactAssessmentResult(models.Model):
    system_operator = models.ForeignKey(SystemOperator, on_delete=models.CASCADE)
    bid = models.ForeignKey(FlexibilityBid, on_delete=models.CASCADE)
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.DjongoManager()
