# Trash-classification

#### Credits to : Wassim ABIDA - Manon CESAIRE - Alann CHERAL - Jasseur HADDED - Clément HARDY

Do you remember the popular sci-fi movie, WALL-E, where robot trash compactors where deployed on Earth to clean the planet after decades of mass consumerism facilitated by a megacorporation ? Even if it seems like an apocalyptic scenario, the movie brought to our notice the harsh environmental reality of today. With the production of almost 1.3 billion tons of waste every day, our interest is to find effective ways to manage our garbages otherwise we could end up in the same position one day. At the same time, policies aimed at empowering and educating people about environmental issues should be in place.

On the one hand, educating children (and not only) about the right things to do in society is very important. We have to learn not to throw your garbage on the floor even if « it is just chewing gum, it does not matter », because if everyone behaves like that, we end up in deplorable situations.

On the other hand, it is necessary to act now, but we must also repair the mistakes made before and find a solution for the tons of waste already thrown away. We have to collect and process garbages. It's not only a question of aesthetics or cleanliness because we don't want to put our feet in a plastic bag at the beach, it is mostly about the protection of the global ecosystem. Indeed, most waste takes years or even thousands of years to decompose.

Seeing the time that rubbish take to be destroyed, we must act quickly because the planet is polluted. We are going to give some examples of the impact of waste on the planet :

  - species extinction, for instance whales or turtles eat plastic bags
  - water pollution, groundwater and rivers contamination
  - soil pollution, lands are less ans less workable lands
  - organic waste cause greenhouse gas emissions (methane, carbon dioxide, ...)
  
Collect garbages becomes essential, we have to avoid mass consumerism and recover waste that can be.


# Business Model

Imagine for a moment that environmental policies as discussed above have been set up and that one of the direct consequences of this would be a smartphone application accessible to all. From this application, the user can on a daily basis take pictures of situations in which there might be an illicit rubbish dump. Then, all of these pictures are collected and sent to a data team who is in charge to analyze them.

The idea is to be able from the data collected, whether or not there are rubbish in the photos, to precisely determine the location where they had been left thanks to a geolocation service when photographes. Besides, in the case of garbages, we want to determine their type because depending on the location or quantity of waste, we will not use the same recovery service. Indeed, in order to protect the location where they had been left, it is necessary to adapt the means used to collect them.

However, there are several constraints that must be respected :

  - to adapt the means used for collecting and then create value from garbages. On the one hand, It may seem naive, but it is not a good idea to send a large vehicle to recover a small amount of waste. On the other hand, it is necessary to take into account the place where these wastes are located with the aim of not deteriorating the environment.
  
  - to minimize the costs of the waste collection. For instance, in France, the waste collection is performed by the municipality so the financial means at their disposal to perform this task are partly dependent on the taxes paid by the taxpayer. Images are collected with GPS coordinates of where they were taken. This removes the repetition of images taken in the same place for a short period of time. All this contibutes to not incur several means for the same rubbish dump and thus to avoid the increase in operating expenses.
  
  - to determine which type the garbages belong to. Indeed, for instance, medical garbages need appropriate ways to be collected and they can not be collected with daily waste.
  

# Submission

You have to test your submissions files before doing your submissions. In that goal, use ramp_test_submission command. Notice that this unit test run in the folder submissions/starting_kit. Before running the test, make sure you have done the following tasks:

  - install ramp-workflow. Go to [`ramp-worflow`](https://github.com/paris-saclay-cds/ramp-workflow) for more help on the [RAMP](http:www.ramp.studio) environment.
  - write the python file image_classifier.py and put it in the following folder [submissions/starting_kit].
  - download the data by excuting python download_data.py
  
You have two possibilities to test your submissions, a complete test (train and test the model with cross validtion like the server or a quick test (just to make sure the submissions code are working). If the test run, print train and test erros on each fold of the cross validation you can then submit to ramp.
