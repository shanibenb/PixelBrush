from trainer import Trainer
import argparse

if __name__ == "__main__":
    # freeze_support()

    parser = argparse.ArgumentParser()
    parser.add_argument("--type", default='deep')
    parser.add_argument("--lr", default=0.0002, type=float)
    parser.add_argument("--l1_coef", default=50, type=float)
    parser.add_argument("--l2_coef", default=100, type=float)
    parser.add_argument("--diter", default=5, type=int)
    parser.add_argument("--cls", default=False, action='store_true')
    parser.add_argument("--vis_screen", default='gan')
    parser.add_argument("--save_path", default='')
    parser.add_argument("--inference", default=False, action='store_true') # train = False, test = True
    parser.add_argument('--pre_trained_disc', default=None)
    parser.add_argument('--pre_trained_gen', default=None)
    parser.add_argument('--dataset', default='oxford')
    parser.add_argument('--split', default=0, type=int) #train is 0, text is 10
    parser.add_argument('--batch_size', default=64, type=int)
    parser.add_argument('--num_workers', default=8, type=int)
    parser.add_argument('--epochs', default=400, type=int)
    args = parser.parse_args()

    trainer = Trainer(type=args.type,
                      dataset=args.dataset,
                      split=args.split,
                      lr=args.lr,
                      diter=args.diter,
                      mode=args.inference,
                      vis_screen=args.vis_screen,
                      l1_coef=args.l1_coef,
                      l2_coef=args.l2_coef,
                      pre_trained_disc=args.pre_trained_disc,
                      pre_trained_gen=args.pre_trained_gen,
                      batch_size=args.batch_size,
                      num_workers=args.num_workers,
                      epochs=args.epochs
                      )


    if not args.inference:
        trainer.train(args.cls)
    else:
        trainer.predict()

