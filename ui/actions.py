from sloth import actions

class ListarComponentes(actions.Action):

    class Meta:
        verbose_name = 'Componentes'

    def view(self):
        data = {'Message': ['Toast'], 'Boxes': ['IconCountBoxes', 'ImageBoxes', 'LinkBoxes', 'TextBoxes', 'TextCountBoxes'], 'Cards': ['ImageCard', 'TextCard'], 'Image': ['Album', 'Carousel', 'Image', 'Slideshow'], 'List': ['AccordionList', 'AvatarList', 'CategoryList', 'HorizontalRuleList', 'IconList', 'LeaderList', 'ListGroup', 'OrderedList'], 'Pills': ['ImagePills', 'TextPills'], 'Progress': ['ProgressBar', 'ProgressCircle'], 'Section': ['ColoredCards', 'CountSecion', 'FeatureSection', 'Hero', 'LeftImageSection', 'PricingSection', 'RightImageSection', 'SimpleCards'], 'Status': ['Status'], 'Steps': ['ArrowSteps', 'BoxSteps', 'HorizontalSteps', 'VerticalSteps'], 'TimeLine': ['TimeLine']}
        return locals()

    def has_permission(self, user):
        return True
